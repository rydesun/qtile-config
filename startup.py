from cffi import FFI
from threading import Thread
import os
import rules
import subprocess
import time

from lib.theme import WallpaperManager
from libqtile import hook


class StartupMgr:
    def __init__(self, env):
        self.env = env
        self.rule_mgr = rules.RuleMgr()
        self.wallpaper_mgr = WallpaperManager(self.env.wallpaper_dir)

    def subreaper(self):
        ffi = FFI()
        ffi.cdef("""
            int prctl(int option, unsigned long arg2);
            #define PR_SET_CHILD_SUBREAPER ...
        """)
        C = ffi.verify("""
            #include<sys/prctl.h>
        """)
        C.prctl(C.PR_SET_CHILD_SUBREAPER, 1)
        def waitpid_thread():
            while True:
                try:
                    os.waitpid(-1, 0)
                except OSError:
                    time.sleep(1)

        thread = Thread(target=waitpid_thread)
        thread.daemon = True
        thread.start()

    def work(self):
        self.rule_mgr.work()

        # init start
        for boot_cmd in self.env.boot_cmds:
            self.boot(boot_cmd)

        # init start and restart
        hook.subscribe.startup(self.wallpaper_mgr.random_set_wallpaper)

    def _boot(self, boot_cmd: list):
        subprocess.Popen(boot_cmd)

    def boot(self, boot_cmd: list):
        hook.subscribe.startup_once(lambda: self._boot(boot_cmd))
