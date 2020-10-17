from libqtile.widget.volume import Volume as _Volume

from .base import TextBox


class Volume(TextBox, _Volume):
    def _update_drawer(self):
        if self.volume <= 0:
            emoji = "婢 "
        else:
            emoji = " "
        self.emoji = False
        super()._update_drawer()
        self.text = emoji + self.text
