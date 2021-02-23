import os
import time
from functools import partial
from threading import Thread

from cffi import FFI
from libqtile import hook

import env
import rules
from lib.theme import WallpaperManager


def startup() -> None:
    subreaper()  # Should not be wrapped by qtile hooks.

    hook.subscribe.client_new(rules.set_window)

    hook.subscribe.client_new(partial(rules.swallow_window, retry=5))
    hook.subscribe.client_killed(rules.unswallow_window)

    wallpaper_mgr = WallpaperManager(env.wallpaper_dir)
    hook.subscribe.startup(wallpaper_mgr.random_set_wallpaper)


# https://blog.lilydjwg.me/2014/2/23/let-s-adopt-orphaned-processes.43035.html
def subreaper() -> None:
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
