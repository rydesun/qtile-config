import psutil
from libqtile.window import Window as _Window


class Window(_Window):
    parent: _Window


def set_window(c: Window):
    wm_class = c.window.get_wm_class()
    wm_window_role = c.window.get_wm_window_role()

    if "fcitx-config-gtk3" in wm_class:
        c.floating = True

    if "firefox" in wm_class:
        if wm_window_role == "Organizer" or wm_window_role == "page-info":
            c.floating = True
        elif wm_window_role == "browser":
            pass

    if "lxappearance" in wm_class:
        c.floating = True

    if "vncviewer" in wm_class:
        c.floating = True

    if "Wine" in wm_class:
        c.floating = True


# https://github.com/qtile/qtile/issues/1771#issuecomment-642065762
def swallow_window(c: Window, retry: int):
    pid = c.window.get_net_wm_pid()
    ppid = psutil.Process(pid).ppid()
    if not ppid:
        return

    cpids = {
        c.window.get_net_wm_pid(): wid
        for wid, c in c.qtile.windows_map.items()
    }
    for _ in range(retry):
        if ppid in cpids:
            parent = c.qtile.windows_map.get(cpids[ppid])
            parent.minimized = True
            c.parent = parent
            return
        ppid = psutil.Process(ppid).ppid()


def unswallow_window(c: Window):
    if hasattr(c, 'parent'):
        c.parent.minimized = False
