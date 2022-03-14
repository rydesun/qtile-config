from libqtile.log_utils import logger
from libqtile.utils import add_signal_receiver

from .battery import Battery


class Kdeconnect(Battery):
    defaults = [
        ("dev_id", "", ""),
        ("dbus_name", "org.kde.kdeconnect", ""),
        ("dbus_path", "/modules/kdeconnect/devices/{dev_id}/battery", ""),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__("", *args, **kwargs)
        self.add_defaults(self.defaults)

    async def _config_async(self):
        self.dbus_path = self.dbus_path.format(dev_id=self.dev_id)
        subscribe = await add_signal_receiver(
            callback=self._signal_received,
            session_bus=True,
            signal_name="refreshed",
            dbus_interface="org.kde.kdeconnect.device.battery",
            bus_name=self.dbus_name,
            path=self.dbus_path,
        )
        if not subscribe:
            logger.warning(
                "Unable to add signal receiver for {}.".format(self.dbus_name)
            )

    def _signal_received(self, message):
        isCharging, percent = message.body
        state = self.BatteryState.Charging if isCharging \
            else self.BatteryState.Discharging
        self.build_string(percent, state)
