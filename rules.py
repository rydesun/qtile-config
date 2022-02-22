import psutil
from libqtile import hook


# https://github.com/qtile/qtile/issues/1771#issuecomment-642065762
@hook.subscribe.client_new
def swallow_window(c, retry=5):
    pid = c.get_pid()
    ppid = psutil.Process(pid).ppid()

    cpids = {
        c.get_pid(): wid
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


@hook.subscribe.client_killed
def unswallow_window(c):
    if hasattr(c, 'parent'):
        c.parent.minimized = False
