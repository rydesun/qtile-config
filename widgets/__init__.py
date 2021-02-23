from libqtile.widget import Wallpaper as _Wallpaper

from .backlight import Backlight
from .base import TextBox, TextButton
from .battery import Battery
from .clock import Clock
from .image_button import ImageButton
from .kdeconnect import Kdeconnect
from .net import Net
from .tasklist import TaskList
from .thermal_sensor import ThermalSensor
from .volume import Volume


class Wallpaper(TextBox, _Wallpaper):
    pass


__all__ = (
    "Backlight",
    "Battery",
    "Clock",
    "ImageButton",
    "Kdeconnect",
    "Net",
    "TaskList",
    "TextBox",
    "TextButton",
    "ThermalSensor",
    "Volume",
    "Wallpaper",
)
