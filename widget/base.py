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
        self.text_offset = 0

        if not self.image_path:
            return
        self.image_path = os.path.expanduser(self.image_path)
        if not os.path.exists(self.image_path):
            logger.warning(f"Image does not exist: {self.image_path}")
            return
        self.image = Img.from_path(self.image_path)
        self.image.theta = self.image_rotate

    def _configure(self, qtile, bar):
        super()._configure(qtile, bar)
        if self.image:
            new_height = self.bar.height - \
                (self.margin_y * 2) - (self.image_padding * 2)
            self.image.resize(height=new_height)

    def calculate_length(self):
        if self.text or self.image:
            return min(
                self.text_offset + self.layout.width,
                self.bar.width,
            ) + self.actual_padding * 2
        else:
            return 0

    def draw(self):
        if not self.can_draw():
            return
        self.drawer.clear(self.background or self.bar.background)

        self.text_offset = 0
        if self.image:
            self.drawer.ctx.save()
            self.drawer.ctx.translate(
                self.margin_x,
                self.margin_y + self.image_padding)
            self.drawer.ctx.set_source(self.image.pattern)
            self.drawer.ctx.paint()
            self.drawer.ctx.restore()

            self.text_offset += self.image.width

        if self.text:
            self.layout.draw(
                self.actual_padding + self.text_offset
                + self.extra_offsetx,
                int(self.bar.height / 2 - self.layout.height / 2) + 1
                + self.extra_offsety
            )

        self.drawer.draw(
            offsetx=self.offsetx,
            offsety=self.offsety,
            width=self.width,
        )
