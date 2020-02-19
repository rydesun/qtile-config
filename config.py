from libqtile import layout, bar, widget
from libqtile.config import (
    Screen, Group, ScratchPad, DropDown,
    EzKey as Key, EzDrag as Drag, EzClick as Click,
)
from libqtile.command import lazy

import env
import theme
import rules
import lib.widgets as mywidget


bring_front_click = True    # bring window topside when clicking


floating_layout=layout.Floating(**theme.layout_floating)
layouts = [
    layout.Columns(**theme.layout_column,
        insert_position=1,
    ),
    layout.Floating(**theme.layout_floating),
]

groups = [
    Group("main", label=" Main", layouts=[layouts[0]], spawn=[env.bin_term]),
    Group("browser", label="龜 Browser", layouts=[layouts[0]], spawn=[env.bin_browser]),
    Group("todo", label=" Todo", layouts=[layouts[0]]),
    Group("float", label=" Float", layouts=[layouts[1]]),
    Group("ghost", label=" Ghost", layouts=[layouts[0]]),
    ScratchPad("scratchpad", [
        DropDown(**theme.dropdown,
            name = "term",
            cmd = env.bin_term,
        ),
    ]),
]

widget_defaults = theme.widget_defaults
screens = [
    Screen(left=bar.Bar([], 500, opacity=0), top=bar.Bar([
        widget.GroupBox(**theme.groupbox,
            visible_groups = ["main", "browser", "todo", "float"],
        ),
        widget.Prompt(**theme.prompt,
            ignore_dups_history = True,
        ),
        widget.Spacer(length=10),
        mywidget.TaskList(**theme.tasklist,
            title_width_method = "uniform",
            highlight_method   = "border",
        ),
        widget.Notify(**theme.notify),
        widget.Systray(icon_size=20),
        widget.Spacer(length=30),
        mywidget.Wlan(**theme.wlan_indicator,
            interface = env.nic_wlan,
            disconnected_message = "", # hide itself if disconnected
        ),
        mywidget.Net(**theme.net_speed,
            interface = [env.nic_lan, env.nic_wlan],
        ),
        widget.Backlight(**theme.blacklight,
            backlight_name = env.backlight,
        ),
        mywidget.Volume(**theme.volume),
        mywidget.ThermalSensor(**theme.thermalSensor),
        mywidget.Clock(**theme.datetime,
            update_interval = 0.5,
        ),
        widget.Spacer(length=10),
    ], **theme.bar)),
    Screen(top=bar.Bar([
        widget.GroupBox(**theme.groupbox,
            visible_groups = ["main", "browser", "todo", "float", "ghost"],
        ),
        mywidget.TaskList(**theme.tasklist,
            title_width_method = "uniform",
            highlight_method   = "border",
        ),
        mywidget.Clock(**theme.datetime,
            update_interval = 0.5,
        ),
        widget.Spacer(length=10),
        ], **theme.bar)),
]

keys = [
    # qtile
    Key("M-S-r", lazy.restart()),
    Key("M-S-q", lazy.shutdown()),

    # terminal emulator
    Key("M-<Return>", lazy.spawn(env.bin_term)),
    Key('M-i', lazy.group['scratchpad'].dropdown_toggle('term')),

    # toggle sidebar
    Key("M-<space>", lazy.hide_show_bar("left")),
    # window focus
    Key("M-j", lazy.layout.down()),
    Key("M-k", lazy.layout.up()),
    Key("M-h", lazy.layout.left()),
    Key("M-l", lazy.layout.right()),
    # window shift
    Key("M-C-j", lazy.layout.shuffle_down()),
    Key("M-C-k", lazy.layout.shuffle_up()),
    Key("M-C-h", lazy.layout.shuffle_left()),
    Key("M-C-l", lazy.layout.shuffle_right()),
    # window resize
    Key("M-S-j", lazy.layout.grow_down()),
    Key("M-S-k", lazy.layout.grow_up()),
    Key("M-S-h", lazy.layout.grow_left()),
    Key("M-S-l", lazy.layout.grow_right()),
    Key("M-n", lazy.layout.normalize()),            # normalize window size
    Key("M-<Tab>", lazy.layout.toggle_split()),     # toggle between stack and split

    Key("M-r", lazy.spawncmd()),
    Key("M-q", lazy.window.toggle_fullscreen()),    # toggle window fullscreen
    Key("M-w", lazy.window.toggle_floating()),      # toggle window floating
    Key("M-e", lazy.spawn(env.bin_hint_window)),    # hint focus
    Key("M-x", lazy.window.kill()),                 # close window
]
for keycode, group in zip("asdfg", ["main", "browser", "todo", "float", "ghost"]):
    keys.extend([
        Key("M-" + keycode, lazy.group[group].toscreen()),
        Key("M-C-" + keycode, lazy.window.togroup(group)),
    ])

mouse = [
    Drag("M-1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag("M-3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
]
