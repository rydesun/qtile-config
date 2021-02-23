from libqtile.widget import Wallpaper as _Wallpaper
from libqtile.widget.image import Image as _Image

from .backlight import Backlight
from .base import TextBox, TextButton
from .battery import Battery
from .clock import Clock
from .kdeconnect import Kdeconnect
from .net import Net
from .tasklist import TaskList
from .thermal_sensor import ThermalSensor
from .volume import Volume


class Wallpaper(TextBox, _Wallpaper):
    pass


class ImageButton(_Image, TextButton):
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
