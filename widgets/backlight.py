import subprocess

from libqtile.widget.backlight import Backlight as _Backlight

from .base import TextBox


class Backlight(TextBox, _Backlight):
    def __init__(self, *args, **kwargs):
        self.defaults.extend((
            ("command_increase", "", ""),
            ("command_decrease", "", ""),
        ))
        super().__init__(*args, **kwargs)

    def poll(self):
        try:
            percent = self._get_info()
        except RuntimeError as e:
            return 'Error: {}'.format(e)

        return self.format.format(percent=percent*100)

    def button_press(self, x, y, button):
        if button == 5:
            subprocess.Popen(self.command_decrease)
        elif button == 4:
            subprocess.Popen(self.command_increase)
