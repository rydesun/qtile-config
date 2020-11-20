from libqtile import hook
import psutil

class RuleMgr:
    def work(self):
        hook.subscribe.client_new(_set_window_float)
        hook.subscribe.client_new(_swallow)
        hook.subscribe.client_killed(_unswallow)


def _set_window_float(c):
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
def _swallow(window):
    pid = window.window.get_net_wm_pid()
    ppid = psutil.Process(pid).ppid()
    cpids = {c.window.get_net_wm_pid(): wid for wid, c in window.qtile.windows_map.items()}
    for _ in range(5):
        if not ppid:
            return
        if ppid in cpids:
            parent = window.qtile.windows_map.get(cpids[ppid])
            parent.minimized = True
            window.parent = parent
            return
        ppid = psutil.Process(ppid).ppid()

def _unswallow(window):
    if hasattr(window, 'parent'):
        window.parent.minimized = False
