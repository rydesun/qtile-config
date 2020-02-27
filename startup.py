import rules
import subprocess

import env
from lib.theme import WallpaperManager
from libqtile import hook


class StartupMgr:
    def __init__(self):
        self.rule_mgr = rules.RuleMgr()
        self.wallpaper_mgr = WallpaperManager(env.wallpaper_dir)

    def work(self):
        self.rule_mgr.work()

        # init start
        for boot_cmd in env.boot_cmds:
            self.boot(boot_cmd)

        # init start and restart
        hook.subscribe.startup(self.wallpaper_mgr.random_set_wallpaper)

    def _boot(self, boot_cmd: list):
        subprocess.Popen(boot_cmd)

    def boot(self, boot_cmd: list):
        hook.subscribe.startup_once(lambda: self._boot(boot_cmd))
