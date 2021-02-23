import subprocess

from libqtile.widget.backlight import Backlight as _Backlight

from .base import TextBox


class Backlight(TextBox, _Backlight):
    def button_press(self, x, y, button):
        if button == 5:
            subprocess.Popen(["brightnessctl", "s", "1%-"])
        elif button == 4:
            subprocess.Popen(["brightnessctl", "s", "+1%"])
