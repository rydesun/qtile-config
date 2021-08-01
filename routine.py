import os
import time
from functools import partial
from threading import Thread

from cffi import FFI
from libqtile import hook

import rules


def startup() -> None:
    subreaper()  # Should not be wrapped by qtile hooks.
    Thread(target=waitpid, args=(5,), daemon=True).start()


def subscribe_hooks() -> None:
    hook.subscribe.client_new(partial(rules.swallow_window, retry=5))
    hook.subscribe.client_killed(rules.unswallow_window)

    @hook.subscribe.client_focus
    def _(c):
        for i in c.qtile.current_group.windows:
            if i.floating:
                i.cmd_bring_to_front()


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

def waitpid(interval: int) -> None:
    while True:
        try:
            os.waitpid(-1, 0)
        except OSError:
            time.sleep(interval)
