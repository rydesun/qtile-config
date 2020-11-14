import subprocess

from libqtile.widget.base import _TextBox


class TextBox(_TextBox):
    def __init__(self, *args, **kwargs):
        self.defaults.extend((
            ("extra_offsetx", 0),
            ("extra_offsety", 0),
            ("execute", ""),
        ))
        super().__init__(*args, **kwargs)

    def draw(self):
        if self.offsetx is None:
            return
        self.drawer.clear(self.background or self.bar.background)
        self.layout.draw(
            (self.actual_padding or 0) + self.extra_offsetx,
            int(self.bar.height / 2.0 - self.layout.height / 2.0) + 1
                # hack
                + self.extra_offsety
        )
        self.drawer.draw(offsetx=self.offsetx, width=self.width)

    def button_press(self, x, y, button):
        if button == 1:
            subprocess.Popen(self.execute)
