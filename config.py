import subprocess
from itertools import chain

import libqtile.hook
from gi.repository import Gio
from libqtile import qtile
from libqtile.config import DropDown, Group, ScratchPad, Screen
from libqtile.layout.columns import Columns
from libqtile.log_utils import logger

import hook
from bar import Bar
from control import Control
from layout import Floating
from lib.env_loader import EnvLoader
from lib.theme_loader import ThemeLoader

# {{{ Init
theme = Gio.Settings.new("org.gnome.desktop.interface").get_string("icon-theme")
if theme:
    try:
        from xdg import Config as XdgConfig

        XdgConfig.setIconTheme(theme)
    except ImportError:
        logger.warning("python-pyxdg not found")

env = EnvLoader()
_control = Control(env)
_bar = Bar(env)
if qtile.core.name == "x11":
    _theme = ThemeLoader(default_file="x11", default_colors_file="x11")
else:
    _theme = ThemeLoader(default_file="wayland", default_colors_file="wayland")
# }}}

# {{{ Qtile config
keys = _control.keys()
mouse = _control.mouse()

if qtile.core.name == "x11":
    main_screen = Screen(bottom=_bar.x11_bar(_theme))
else:
    main_screen = Screen(bottom=_bar.wayland_bar(_theme))
screens = [main_screen]

for _ in range(env.total_screens - 1):
    another_screen = Screen(bottom=_bar.other_bar(_theme))
    screens.append(another_screen)

layouts = [Columns(insert_position=1, **_theme.layout_column)]
groups = [Group(name=i["key"], label="⬤") for i in env.groups]

_dropdowns = [
    DropDown(i["name"], i["cmd"], **_theme.dropdown_window) for i in env.dropdowns
]
_scratch_pad = ScratchPad("default", _dropdowns)
groups.append(_scratch_pad)

floating_layout = Floating(
    float_rules=env.float_rules,
    float_config=env.float_config,
    **_theme.layout_floating,
)

widget_defaults = _theme.widget_defaults
# }}}

# {{{ Hooks
if qtile.core.name == "x11":
    rules = chain(Floating.default_float_rules, env.float_rules)
    hook.float_window.register(rules)

if qtile.core.name == "x11":
    hook.xprop.register()

hook.swallow_window.register()
# }}}


@libqtile.hook.subscribe.startup_once
def autostart():
    cmd_env = ["dbus-update-activation-environment", "--systemd", "--all"]
    subprocess.Popen(cmd_env)
    if qtile.core.name == "x11":
        cmd_sysmted = ["systemctl", "start", "--user", "X11.target"]
        subprocess.Popen(cmd_sysmted)
    else:
        cmd_sysmted = ["systemctl", "start", "--user", "Wayland.target"]
        subprocess.Popen(cmd_sysmted)

        from pathlib import Path

        cmd_xwayland = ["xrdb", "-merge", Path.home() / ".xresources"]
        subprocess.Popen(cmd_xwayland)


@libqtile.hook.subscribe.shutdown
def shutdown():
    cmd_sysmted = ["systemctl", "stop", "--user", "graphical-session.target"]
    subprocess.Popen(cmd_sysmted)


# vim:fdm=marker
