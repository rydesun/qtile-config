from itertools import chain

import psutil
from libqtile import hook
from libqtile.config import DropDown, Group, ScratchPad, Screen
from libqtile.layout.columns import Columns
from libqtile.log_utils import logger
from libqtile.utils import send_notification

from bar import Bar
from color import Color
from control import Control
from layout import Floating
from theme import Theme

try:
    import env
except ImportError:
    logger.warning("env.py is missing")
    send_notification("Configuration warning",
                      "env.py is missing. Use env_example.py instead.")
    import env_example as env

control_agent = Control(env)
bar_agent = Bar(env)
main_theme = Theme(
    Color(),
    scale_factor=env.main_screen_scale,
)

# ==== Qtile config begin ====

screens = [
    Screen(
        top=bar_agent.main_bar(theme=main_theme),
    ),
    *(
        Screen(
            top=bar_agent.other_bar(theme=Theme(
                Color(), scale_factor=env.other_screen_scale,
            )),
        ) for _ in range(1, getattr(env, "total_screens", 1))
    ),
]

layouts = [
    Columns(
        insert_position=1,
        **main_theme.layout_column),
    Floating(**main_theme.layout_floating),
]

keys = control_agent.keys(
    group_chars="asdf",
    scratchpad_names=env.cmd_dropdown[::2]
)
mouse = control_agent.mouse()

groups = [
    Group("a", label="⬤", layouts=[layouts[0]]),
    Group("s", label="⬤", layouts=[layouts[0]], spawn=[env.cmd_browser]),
    Group("d", label="⬤", layouts=[layouts[0]]),
    Group("f", label="⬤", layouts=[layouts[1]]),
    ScratchPad("scratchpad", [
        DropDown(
            name=name,
            cmd=cmd,
            **main_theme.dropdown_window)
        for name, cmd in zip(env.cmd_dropdown[::2], env.cmd_dropdown[1::2])
    ]),
]

widget_defaults = main_theme.widget_defaults

floating_layout = Floating(
    float_config=env.float_config,
    **main_theme.layout_floating)


# ==== hooks ====
@hook.subscribe.client_new
def match_floating(c):
    for rule in chain(Floating.default_float_rules, env.float_rules):
        if c.match(rule):
            c.match_floating = True
            return
    c.match_floating = False


# https://github.com/qtile/qtile/issues/1771#issuecomment-642065762
@hook.subscribe.client_new
def swallow_window(c, retry=5):
    if c.match_floating:
        return
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
