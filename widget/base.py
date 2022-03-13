import os

from libqtile.images import Img
from libqtile.log_utils import logger
from libqtile.widget.base import _TextBox


class Box(_TextBox):
    defaults = [
        ("image_path", "", ""),
        ("image_padding", 0, ""),
        ("image_rotate", 0.0, ""),
        ("extra_offsetx", 0, ""),
        ("extra_offsety", 0, ""),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_defaults(Box.defaults)

        self.image = None
        self.image_length = 0
        if not self.image_path:
            return
        self.image_path = os.path.expanduser(self.image_path)
        if not os.path.exists(self.image_path):
            logger.warning(f"Image does not exist: {self.image_path}")
            return
        self.image = Img.from_path(self.image_path)
        self.image.theta = self.image_rotate

    def calculate_length(self):
        if self.text:
            return min(
                self.image_length + self.layout.width, self.bar.width
            ) + self.actual_padding * 2
        else:
            return 0

    def draw(self):
        if not self.can_draw():
            return

        self.image_length = 0
        if self.image:
            new_height = self.bar.height - \
                (self.margin_y * 2) - (self.image_padding * 2)
            self.image.resize(height=new_height)
            self.drawer.clear(self.background or self.bar.background)
            self.drawer.ctx.save()
            self.drawer.ctx.translate(
                self.margin_x,
                self.margin_y + self.image_padding)
            self.drawer.ctx.set_source(self.image.pattern)
            self.drawer.ctx.paint()
            self.drawer.ctx.restore()
            self.image_length += self.image.width

        if self.text:
            self.drawer.clear(self.background or self.bar.background)
            self.layout.draw(
                (self.actual_padding or 0) + self.image_length
                + self.extra_offsetx,
                int(self.bar.height / 2 - self.layout.height / 2) + 1
                + self.extra_offsety
            )

        self.drawer.draw(
            offsetx=self.offsetx,
            offsety=self.offsety,
            width=self.width,
        )
