from libqtile.widget.backlight import Backlight as _Backlight

from .base import Box


class Backlight(Box, _Backlight):
    def _get_info(self):
        return super()._get_info() * 100
