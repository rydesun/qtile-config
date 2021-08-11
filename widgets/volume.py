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
        if self.volume < 0:
            self.text = '{}{}'.format(self.icon_mute, "M")
        else:
            self.text = '{}{}'.format(self.icon, self.volume)

    def button_press(self, x, y, button):
        if button == 5:
            subprocess.Popen(self.volume_down_command)
        elif button == 4:
            subprocess.Popen(self.volume_up_command)
        elif button == 1:
            subprocess.Popen(self.mute_command)
