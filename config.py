import psutil
from libqtile import hook
from libqtile.config import DropDown, Group, ScratchPad, Screen
from libqtile.layout.columns import Columns
from libqtile.log_utils import logger
from libqtile.utils import send_notification

import color
from bar import Bar
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

theme_agent = Theme(color)
bar_agent = Bar(env)
control_agent = Control(env)

# ==== Qtile config begin ====

keys = control_agent.keys(group_chars="asdf")
mouse = control_agent.mouse()

screens = [
    Screen(top=bar_agent.main_bar(theme=theme_agent)),
    Screen(top=bar_agent.other_bar(theme=theme_agent)),
]

layouts = [
    Columns(
        insert_position=1,
        **theme_agent.layout_column),
    Floating(**theme_agent.layout_floating),
]

groups = [
    Group("a", label="⬤", layouts=[layouts[0]], spawn=[env.cmd_term]),
    Group("s", label="⬤", layouts=[layouts[0]], spawn=[env.cmd_browser]),
    Group("d", label="⬤", layouts=[layouts[0]]),
    Group("f", label="⬤", layouts=[layouts[1]]),
    ScratchPad("scratchpad", [
        DropDown(
            name="term",
            cmd=env.cmd_term_alter,
            **theme_agent.dropdown_window),
        DropDown(
            name="note",
            cmd=env.cmd_note,
            **theme_agent.dropdown_window),
    ]),
]

widget_defaults = theme_agent.widget_defaults

floating_layout = Floating(
    float_rules=env.float_rules,
    float_config=env.float_config,
    **theme_agent.layout_floating)


# ==== hooks ====

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
