import asyncio
from enum import Enum, auto
import subprocess

from dbus_next.aio.message_bus import MessageBus
from dbus_next.constants import BusType
from libqtile.log_utils import logger
from libqtile.utils import add_signal_receiver, send_notification

from .base import Box
from .decoration import inject_decorations


@inject_decorations
class Battery(Box):
    class BatteryState(Enum):
        Charging = auto()
        Discharging = auto()
        Plugging = auto()

    defaults = [
        ("sep", (85, 65, 40, 25, 0), ""),
        ("alarm_threshold", 20, ""),
        ("alarm_interval", 600, ""),
        ("hibernate_threshold", 5, ""),
        ("hibernate_countdown", 120, ""),
        ("icon_charge", "", ""),
        ("icon_plug", "", ""),
        ("icon_full_energy", "", ""),
        ("icon_high_energy", "", ""),
        ("icon_half_energy", "", ""),
        ("icon_low_energy", "", ""),
        ("icon_empty_energy", "", ""),
        ("foreground", "", ""),
        ("foreground_discharge", "", ""),
        ("foreground_low", "", ""),
        ("dbus_name", "org.freedesktop.UPower", ""),
        ("dbus_path", "/org/freedesktop/UPower/devices/DisplayDevice", ""),
        ("dbus_props", "org.freedesktop.UPower.Device", "")
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_defaults(Battery.defaults)
        self.alarm = asyncio.create_task(asyncio.sleep(self.alarm_interval))
        self.hibernate_lock = asyncio.Lock()

    async def _config_async(self):
        bus = await MessageBus(bus_type=BusType.SYSTEM).connect()
        introspect = await bus.introspect(self.dbus_name, self.dbus_path)
        obj = bus.get_proxy_object(self.dbus_name, self.dbus_path, introspect)
        self.props = obj.get_interface(self.dbus_props)

        max = await self.props.get_energy_full()
        if max <= 0:
            # Not have a battery
            return

        subscribe = await add_signal_receiver(
            callback=self._signal_received,
            signal_name="PropertiesChanged",
            dbus_interface="org.freedesktop.DBus.Properties",
            bus_name=self.dbus_name,
            path=self.dbus_path,
        )
        if not subscribe:
            logger.warning(
                "Unable to add signal receiver for {}.".format(self.dbus_name)
            )
        await self.get_info()

    def _signal_received(self, _):
        self.qtile.call_soon(asyncio.create_task, self.get_info())

    async def get_info(self):
        percent, state = await self._get_info()
        self.build_string(percent, state)
        await self.trigger(percent, state)

    async def _get_info(self):
        percent = await self.props.get_percentage()
        state = await self.props.get_state()
        if state == 1:
            state = self.BatteryState.Charging
        elif state == 2:
            state = self.BatteryState.Discharging
        else:
            state = self.BatteryState.Plugging
        return percent, state

    def build_string(self, percent, state):
        percent = min(max(0, percent), 100)

        if self.layout is not None:
            if state == self.BatteryState.Discharging:
                if percent < self.low_percentage:
                    self.layout.colour = self.foreground_low
                else:
                    self.layout.colour = self.foreground_discharge
            else:
                self.layout.colour = self.foreground

        icon = None
        for i, threshold in zip((
                self.icon_full_energy,
                self.icon_high_energy,
                self.icon_half_energy,
                self.icon_low_energy,
                self.icon_empty_energy,
            ),
           self.sep):
            if percent >= threshold:
                icon = i
                break

        if state == self.BatteryState.Charging:
            extra_icon = self.icon_charge
        elif state == self.BatteryState.Discharging:
            extra_icon = self.icon_discharge
        elif state == self.BatteryState.Plugging:
            extra_icon = self.icon_plug
        else:
            extra_icon = ""

        text = self.format.format(
            icon=icon,
            extra_icon=extra_icon,
            percent=percent,
        )
        self.update(text)

    async def trigger(self, percent, state):
        if state != self.BatteryState.Discharging:
            return
        if percent <= self.alarm_threshold \
            and (not self.alarm or self.alarm.done()):
            send_notification("低电量", f"电量还剩{percent:.0f}%")
            self.alarm = asyncio.create_task(asyncio.sleep(self.alarm_interval))
        if percent <= self.hibernate_threshold:
            await self.hibernate()

    async def hibernate(self):
        if self.hibernate_lock.locked():
            return
        await self.hibernate_lock.acquire()
        send_notification("低电量", "电量过低，即将休眠")
        await asyncio.sleep(self.hibernate_countdown)
        percent, state = await self._get_info()
        if state == self.BatteryState.Discharging \
            and percent <= self.hibernate_threshold:
            subprocess.run(["systemctl", "-i", "hibernate"])
        self.hibernate_lock.release()
