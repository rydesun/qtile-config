import subprocess

from libqtile.widget.volume import Volume as _Volume

from .base import TextBox


class Volume(TextBox, _Volume):
    def __init__(self, *args, **kwargs):
        self.defaults.extend((
            ("icon", "", ""),
            ("icon_mute", "", ""),
        ))
        super().__init__(*args, **kwargs)

    def _update_drawer(self):
        self.emoji = False
        super()._update_drawer()
        if self.volume <= 0:
            self.text = self.icon_mute + 'Mute'
        else:
            self.text = self.icon + self.text

    def button_press(self, x, y, button):
        if button == 5:
            subprocess.Popen(self.volume_down_command)
        elif button == 4:
            subprocess.Popen(self.volume_up_command)
        elif button == 1:
            subprocess.Popen(self.mute_command)
