from libqtile import hook


class RuleMgr:
    def work(self):
        hook.subscribe.client_new(_set_window_float)


def _set_window_float(c):
    wm_class = c.window.get_wm_class()
    wm_window_role = c.window.get_wm_window_role()

    if "firefox" in wm_class:
        if wm_window_role == "Organizer" or wm_window_role == "page-info":
            c.floating = True
        elif wm_window_role == "browser":
            pass
