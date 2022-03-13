from libqtile.widget.pulse_volume import PulseVolume as _PulseVolume

from .base import Box


class PulseVolume(Box, _PulseVolume):
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
