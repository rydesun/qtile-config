from libqtile.widget.backlight import Backlight as _Backlight

from .base import TextBox


class Backlight(TextBox, _Backlight):
    pass
