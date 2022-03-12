from libqtile.log_utils import logger
from libqtile.utils import add_signal_receiver

from .base import Box


class Kdeconnect(Box):
    def __init__(self, *args, **kwargs):
        self.defaults.extend((
            ('low_percentage', 0.20, ""),
            ('format', '{char} {percent: .0f}', 'Display format'),
            ("sep", (0.85, 0.65, 0.4, 0.25), ""),
            ("icon_charge", "", ""),
            ("icon_full_energy", "", ""),
            ("icon_high_energy", "", ""),
            ("icon_half_energy", "", ""),
            ("icon_low_energy", "", ""),
            ("icon_empty_energy", "", ""),
            ("foreground", "", ""),
            ("foreground_low", "", ""),
            ("dev_id", "", ""),
            ("dbus_name", "org.kde.kdeconnect", ""),
            ("dbus_path", "/modules/kdeconnect/devices/{dev_id}/battery", ""),
        ))
        super().__init__("", *args, **kwargs)

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
        isCharging, charge = message.body
        percent = charge / 100

        if self.layout is not None:
            if percent < self.low_percentage:
                self.layout.colour = self.foreground_low
            else:
                self.layout.colour = self.foreground
        if isinstance(self.sep, tuple) and len(self.sep) == 4:
            if percent >= self.sep[0]:
                icon = self.icon_full_energy
            elif percent >= self.sep[1]:
                icon = self.icon_high_energy
            elif percent >= self.sep[2]:
                icon = self.icon_half_energy
            elif percent >= self.sep[3]:
                icon = self.icon_low_energy
            else:
                icon = self.icon_empty_energy
        else:
            icon = self.icon_full_energy

        if isCharging:
            extra_icon = self.icon_charge
        else:
            extra_icon = self.icon_discharge

        text = self.format.format(
            icon=icon,
            percent=percent*100 if percent < 1 else 100,
            extra_icon=extra_icon,
        )
        self.update(text)
