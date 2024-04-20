from itertools import chain

from libqtile import qtile
from libqtile.config import DropDown, Group, ScratchPad, Screen
from libqtile.layout.columns import Columns
from libqtile.log_utils import logger
from libqtile.utils import send_notification

import hook
from bar import Bar
from control import Control
from layout import Floating
from lib.env_loader import EnvLoader
from lib.theme_loader import ThemeLoader

# {{{ Init
try:
    from xdg import Config as XdgConfig
    XdgConfig.setIconTheme('Papirus')
    XdgConfig.setIconSize(16)
except ImportError:
    logger.warning("python-pyxdg not found")
    send_notification("Configuration warning", "python-pyxdg not found")

env = EnvLoader()
theme = ThemeLoader()
control_agent = Control(env)
bar_agent = Bar(env)
main_theme = theme
other_theme = theme
# }}}

# {{{ Qtile config
keys = control_agent.keys()
mouse = control_agent.mouse()

screens = [
    Screen(top=bar_agent.main_bar(main_theme)),
    *(Screen(top=bar_agent.other_bar(other_theme))
      for _ in range(env.total_screens-1)),
]

layouts = [
    Columns(insert_position=1, **main_theme.layout_column)
]

groups = [Group(name=i["key"], label="⬤") for i in env.groups]
groups.append(
    ScratchPad("default_scratchpad", [
        DropDown(i["name"], i["cmd"], **main_theme.dropdown_window)
        for i in env.dropdowns]))

floating_layout = Floating(
    float_rules=env.float_rules,
    float_config=env.float_config,
    **main_theme.layout_floating)

widget_defaults = main_theme.widget_defaults
# }}}

# {{{ Hooks
if qtile.core.name == "x11":
    rules = chain(Floating.default_float_rules, env.float_rules)
    hook.float_window.register(rules)

if qtile.core.name == "x11":
    hook.xprop.register()

hook.swallow_window.register()
# }}}


import subprocess
import libqtile.hook
@libqtile.hook.subscribe.startup_once
def autostart():
    cmd = ["systemctl", "start", "--user"]
    if qtile.core.name == "x11":
        cmd.append("X11.target")
    else:
        cmd.append("Wayland.target")
    subprocess.Popen(cmd).wait()

# vim:fdm=marker
