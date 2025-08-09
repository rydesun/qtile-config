# https://github.com/qtile/qtile/issues/1771#issuecomment-642065762

import psutil
from libqtile import hook


def register():
    hook.subscribe.client_new(swallow_window)
    hook.subscribe.client_killed(unswallow_window)


def swallow_window(c, retry=5):
    if getattr(c, 'floating', True) or getattr(c, 'match_floating', False):
        return

    pid = c.get_pid()
    ppid = psutil.Process(pid).ppid()

    cpids = {
        c.get_pid(): wid
        for wid, c in c.qtile.windows_map.items()
        if hasattr(c, 'get_pid')
    }
    for _ in range(retry):
        if not ppid:
            return
        if ppid in cpids:
            parent = c.qtile.windows_map.get(cpids[ppid])
            parent.minimized = True
            parent._swallowed = True
            c.parent = parent
            return
        ppid = psutil.Process(ppid).ppid()


def unswallow_window(c):
    if hasattr(c, 'parent') and c.parent._swallowed:
        c.parent.minimized = False
        c.parent._swallowed = False
