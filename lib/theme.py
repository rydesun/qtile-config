import os
import random
import subprocess


class WallpaperManager:
    def __init__(self, dirpath):
        self.dirpath = dirpath
        self.list = []

    def set_wallpaper(self, file):
        path = os.path.join(self.dirpath, file)
        cmd_set_wallpaper = ["hsetroot", "-cover", path]
        subprocess.Popen(cmd_set_wallpaper)

    def find_resources(self):
        files = os.listdir(self.dirpath)
        return [f for f in files if os.path.isfile(os.path.join(self.dirpath, f))]

    def random_choice(self):
        files = self.find_resources()
        if len(files) == 0:
            return
        random.shuffle(files)
        invalid_files = [i for i in self.list for j in files if i == j]
        new_files = [i for i in files if i not in self.list]
        self.list = new_files + invalid_files

        idx = random.randrange(len(self.list)//2)
        file = self.list.pop(idx)
        self.list.append(file)
        return file

    def random_set_wallpaper(self):
        file = os.path.join(self.dirpath, self.random_choice())
        self.set_wallpaper(file)
