import subprocess

from libqtile.widget.image import Image as _Image


class ImageButton(_Image):
    def __init__(self, *args, **kwargs):
        self.defaults.extend((
            ("execute", ""),
        ))
        super().__init__(*args, **kwargs)

    def button_press(self, x, y, button):
        if button == 1:
            subprocess.Popen(self.execute)
