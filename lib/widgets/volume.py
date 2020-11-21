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
