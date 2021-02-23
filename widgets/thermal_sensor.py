from libqtile.widget.sensors import ThermalSensor as _ThermalSensor

from .base import TextBox


class ThermalSensor(TextBox, _ThermalSensor):
    def __init__(self, *args, **kwargs):
        self.defaults.extend((
            ("icon", "", ""),
        ))
        super().__init__(*args, **kwargs)

    def poll(self):
        return self.icon + super().poll()
