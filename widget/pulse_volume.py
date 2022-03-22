from libqtile.widget.pulse_volume import PulseVolume as _PulseVolume

from .base import Box


class PulseVolume(Box, _PulseVolume):
    defaults = [
        ("icon", "", ""),
        ("icon_mute", "", ""),
        ("icon_headphone", "", ""),
        ("icon_headphone_mute", "", ""),
        ("dev_headphone_sinks", [], ""),
        ("mute_text", "M", ""),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_defaults(self.defaults)

    def _update_drawer(self):
        if self.volume < 0:
            volume = self.mute_text
            if self.default_sink_name in self.dev_headphone_sinks:
                icon = self.icon_headphone_mute
            else:
                icon = self.icon_mute
        else:
            volume = self.volume
            if self.default_sink_name in self.dev_headphone_sinks:
                icon = self.icon_headphone
            else:
                icon = self.icon
        self.text = '{}{}'.format(icon, volume)
