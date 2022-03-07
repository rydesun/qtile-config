import os
from glob import glob

from libqtile.widget.base import InLoopPollText

from .base import TextBox


class ThermalSensor(TextBox, InLoopPollText):
    def __init__(self, *args, **kwargs):
        self.defaults.extend((
            ("dev_name", "acpitz", ""),
            ("sysfs_glob", "/sys/class/hwmon/hwmon*", ""),
            ("update_interval", 2, "Update interval in seconds"),
            ("threshold", 70, ""),
            ("foreground_alert", "ff0000", "Foreground colour alert"),
            ("icon", "", ""),
        ))
        super().__init__(*args, **kwargs)

        dir = self._get_sysfs_path()
        if dir is None:
            return
        self.file = open(os.path.join(dir, "temp1_input"))

    def _get_sysfs_path(self):
        for path in glob(self.sysfs_glob):
            name = os.path.join(path, "name")
            with open(name) as f:
                if self.dev_name == f.read().rstrip():
                    return path

    def get_temperature(self):
        temp = round(int(self.file.read().rstrip()) / 1000)
        self.file.seek(0)
        return temp

    def poll(self):
        temp = self.get_temperature()
        if temp >= self.threshold:
            self.layout.colour = self.foreground_alert
        else:
            self.layout.colour = self.foreground
        return f'{self.icon}{temp}°C'
