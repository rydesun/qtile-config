from libqtile.widget.volume import Volume as _Volume

from .base import Box


class Volume(Box, _Volume):
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
