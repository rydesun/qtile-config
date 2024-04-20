from libqtile.widget.pulse_volume import PulseVolume as _PulseVolume
from libqtile.widget.pulse_volume import pulse

from .base import Box
from .decoration import inject_decorations


@inject_decorations
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
        if self.volume is None:
            return
        if self.volume < 0:
            volume = self.mute_text
            if self.is_headphone():
                icon = self.icon_headphone_mute
            else:
                icon = self.icon_mute
        else:
            volume = self.volume
            if self.is_headphone():
                icon = self.icon_headphone
            else:
                icon = self.icon
        self.text = f'{icon}{volume}'

    def is_headphone(self) -> bool:
        if not pulse.default_sink_name or not pulse.default_sink:
            return False
        return pulse.default_sink_name in self.dev_headphone_sinks \
            or "headphone" in pulse.default_sink.port_active.name.lower()
