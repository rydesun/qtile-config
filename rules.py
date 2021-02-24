import psutil
from libqtile.window import Window as _Window


class Window(_Window):
    parent: _Window


# https://github.com/qtile/qtile/issues/1771#issuecomment-642065762
def swallow_window(c: Window, retry: int):
    pid = c.window.get_net_wm_pid()
    ppid = psutil.Process(pid).ppid()

    cpids = {
        c.window.get_net_wm_pid(): wid
        for wid, c in c.qtile.windows_map.items()
    }
    for _ in range(retry):
        if not ppid:
            return
        if ppid in cpids:
            parent = c.qtile.windows_map.get(cpids[ppid])
            parent.minimized = True
            c.parent = parent
            return
        ppid = psutil.Process(ppid).ppid()


def unswallow_window(c: Window):
    if hasattr(c, 'parent'):
        c.parent.minimized = False
