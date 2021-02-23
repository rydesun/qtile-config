from libqtile.widget.sensors import ThermalSensor as _ThermalSensor

from .base import TextBox


class ThermalSensor(TextBox, _ThermalSensor):
    def poll(self):
        return " " + super().poll()
