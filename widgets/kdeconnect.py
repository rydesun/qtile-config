import dbus
from dbus.mainloop.glib import DBusGMainLoop
from libqtile.widget.base import ThreadPoolText

from .base import TextBox


class Kdeconnect(TextBox, ThreadPoolText):
    def __init__(self, *args, **kwargs):
        self.defaults.extend((
            ('low_percentage', 0.20),
            ('format', '{char} {percent: .0f}', 'Display format'),
            ("sep", (0.85, 0.65, 0.4, 0.25)),
            ("icon_charge", ""),
            ("icon_full_energy", ""),
            ("icon_high_energy", ""),
            ("icon_half_energy", ""),
            ("icon_low_energy", ""),
            ("icon_empty_energy", ""),
            ("foreground", ""),
            ("foreground_low", ""),
            ("dev_id", ""),
            ("dbus_name", "org.kde.kdeconnect"),
            ("dbus_path", "/modules/kdeconnect/devices/{dev_id}/battery"),
        ))
        super().__init__("", *args, **kwargs)
        self._dbus_init()

    def _dbus_init(self):
        dbus_loop = DBusGMainLoop()
        if hasattr(self, 'dbus'):
            return
        self.dbus = dbus.SessionBus(mainloop=dbus_loop)
        dbus_path = self.dbus_path.format(dev_id=self.dev_id)
        try:
            self.dev = self.dbus.get_object(self.dbus_name, dbus_path)
        except Exception:
            self.dev = None

    def poll(self) -> str:
        if not self.dev:
            return ""
        try:
            data = self.dev.GetAll("charge")
        except dbus.exceptions.DBusException:
            return ""
        percent = data["charge"] / 100
        isCharging = data["isCharging"]
        return self.build_string(percent, isCharging)

    def build_string(self, percent, isCharging):
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

        return self.format.format(
            icon=icon,
            percent=percent*100 if percent < 1 else 100,
            extra_icon=extra_icon,
        )
