from libqtile.widget import Net as _Net


def humanize_bytes(value):
    suff = ["B", "K", "M", "G", "T"]
    while value >= 1024 and len(suff) > 1:
        value /= 1024
        suff.pop(0)
    if value > 921:
        value /= 1024
        suff.pop(0)
    return value, suff[0]


class Net(_Net):
    _Net.defaults.extend((
        ("icon_upload", ""),
        ("icon_download", ""),
        ("fmt", "{icon_download} {txt_download} {icon_upload} {txt_upload}"),
        ("fmt_txt", "{:·>3.0f}{}"),
        ("mini_val_threshold", 100),
        ("fmt_mini", "···B"),
        ("fmt_zero", "····"),
    ))

    def poll(self):
        new_int = self.get_stats()
        down = 0; up = 0
        for interface in self.interface:
            down += new_int[interface]['down'] - \
                self.interfaces[interface]['down']
            up += new_int[interface]['up'] - \
                self.interfaces[interface]['up']
        down /= self.update_interval
        up /= self.update_interval
        self.interfaces = new_int

        txt_download = ""; txt_upload = ""
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

        return self.fmt.format(
            icon_download=self.icon_download,
            txt_download=txt_download,
            icon_upload=self.icon_upload,
            txt_upload=txt_upload)
