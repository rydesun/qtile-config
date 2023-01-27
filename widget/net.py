from fnmatch import fnmatch

from libqtile.widget.net import Net as _Net

from .base import Box
from .decoration import inject_decorations


def humanize_bytes(value):
    suff = ["B", "K", "M", "G", "T"]
    while value >= 1024 and len(suff) > 1:
        value /= 1024
        suff.pop(0)
    if value > 921:
        value /= 1024
        suff.pop(0)
    return value, suff[0]


@inject_decorations
class Net(Box, _Net):
    defaults = [
        ("icon_upload", "", ""),
        ("icon_download", "", ""),
        ("format",
         "{icon_download} {txt_download}  {icon_upload} {txt_upload}", ""),

        ("fmt_zero", "··· ·", ""),
        ("fmt_mini", "··· ●", ""), ("mini_val_threshold", 10_000, ""),
        ("fmt_txt", "{:·>3.0f} {}", ""),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_defaults(self.defaults)

    def filter(self, interface) -> bool:
        for pat in self.interface:
            if fnmatch(interface, pat):
                return True
        return False

    def poll(self):
        new_int = self.get_stats()
        down = 0
        up = 0
        for interface in new_int:
            if not self.filter(interface):
                continue
            down += new_int[interface]['down'] - \
                self.stats[interface]['down']
            up += new_int[interface]['up'] - \
                self.stats[interface]['up']
        down /= self.update_interval
        up /= self.update_interval
        self.stats = new_int

        txt_download = ""
        txt_upload = ""
        if down == 0:
            txt_download = self.fmt_zero
        elif down < self.mini_val_threshold:
            txt_download = self.fmt_mini
        else:
            down, down_unit = humanize_bytes(down)
            txt_download = self.fmt_txt.format(down, down_unit)
        if up == 0:
            txt_upload = self.fmt_zero
        elif up < self.mini_val_threshold:
            txt_upload = self.fmt_mini
        else:
            up, up_unit = humanize_bytes(up)
            txt_upload = self.fmt_txt.format(up, up_unit)

        return self.format.format(
            icon_download=self.icon_download,
            txt_download=txt_download,
            icon_upload=self.icon_upload,
            txt_upload=txt_upload)
