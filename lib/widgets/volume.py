import subprocess

from libqtile.widget.volume import Volume as _Volume

from .base import TextBox


class Volume(TextBox, _Volume):
    def _update_drawer(self):
        self.emoji = False
        super()._update_drawer()
        if self.volume <= 0:
            self.text = '婢 Mute'
        else:
            self.text = " " + self.text

    def button_press(self, x, y, button):
        if button == 5:
            subprocess.Popen(["amixer", "-q", "sset", "Master", "1%-"])
        elif button == 4:
            subprocess.Popen(["amixer", "-q", "sset", "Master", "1%+"])
        elif button == 1:
            subprocess.Popen(["amixer", "-q", "sset", "Master", "toggle"])
