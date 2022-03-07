import asyncio

from dbus_next.aio.message_bus import MessageBus
from dbus_next.constants import BusType
from libqtile.log_utils import logger
from libqtile.utils import add_signal_receiver

from .base import TextBox


class BatteryState:
    Charging = 1
    Discharing = 2


class Battery(TextBox):
    def __init__(self, *args, **kwargs):
        self.defaults.extend((
            ("sep", (0.85, 0.65, 0.4, 0.25, 0), ""),
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
        ))
        super().__init__(*args, **kwargs)

    async def _config_async(self):
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
        bus = await MessageBus(bus_type=BusType.SYSTEM).connect()
        introspect = await bus.introspect(self.dbus_name, self.dbus_path)
        obj = bus.get_proxy_object(self.dbus_name, self.dbus_path, introspect)
        self.props = obj.get_interface(self.dbus_props)

        await self.build_string()

    def _signal_received(self, _):
        self.qtile.call_soon(asyncio.create_task, self.build_string())

    async def build_string(self):
        percent = await self.props.get_percentage()
        state = await self.props.get_state()

        percent = min(max(0, percent), 100)

        if self.layout is not None:
            if state == BatteryState.Discharing:
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

        if state == BatteryState.Charging:
            extra_icon = self.icon_charge
        elif state == BatteryState.Discharing:
            extra_icon = self.icon_discharge
        else:
            extra_icon = ""

        text = self.format.format(
            icon=icon,
            extra_icon=extra_icon,
            percent=percent,
        )
        self.update(text)
