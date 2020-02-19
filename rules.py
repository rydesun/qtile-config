import subprocess

from libqtile import hook

import env


@hook.subscribe.client_new
def set_window_float(c):
    wm_class = c.window.get_wm_class()
    wm_window_role = c.window.get_wm_window_role()

    if "firefox" in wm_class:
        if wm_window_role == "Organizer" or wm_window_role == "page-info":
            c.floating = True
        elif wm_window_role == "browser":
            pass
