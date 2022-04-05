import os
import random

from .base import Box
from .decoration import inject_decorations


@inject_decorations
class Wallpaper(Box):
    defaults = [
        ("default", "", "Default wallpaper"),
        ("dir", "", "Wallpaper Directory"),
        ("mode", "fill", "fill or stretch"),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_defaults(self.defaults)
        self.add_callbacks({"Button1": self.random_wallpaper})
        self.default = str(os.path.expanduser(self.default))
        self.dir = str(os.path.expanduser(self.dir))
        self.used_images = set()

    def _configure(self, qtile, bar):
        super()._configure(qtile, bar)
        if self.default:
            self.used_images.add(self.default)
            self.set_wallpaper(self.default)
        else:
            self.random_wallpaper()

    def is_valid(self, path):
        ext = os.path.splitext(path)[1]
        if ext.lower() not in (".png", ".jpg", ".jpeg"):
            return False
        return os.path.isfile(path)

    def images(self):
        if not self.dir:
            return []
        files = os.listdir(self.dir)
        return filter(self.is_valid,
                      (os.path.join(self.dir, i) for i in files))

    def random_wallpaper(self):
        image = self.random_choice()
        if image is None:
            return
        self.set_wallpaper(image)

    def set_wallpaper(self, image) -> None:
        self.qtile.paint_screen(self.bar.screen, image, self.mode)

    def random_choice(self):
        images = set(self.images())

        # Remove non-existent images
        self.used_images.intersection_update(images)

        if len(images) == 0:
            return

        unused_images = tuple(images - self.used_images)
        if len(unused_images) == 0:
            # Restart if exhausted
            unused_images = tuple(self.used_images)
            self.used_images = set()

        image = random.choice(unused_images)
        self.used_images.add(image)
        return image
