import env

from libqtile import bar, layout, widget
from libqtile.command import lazy
from libqtile.config import DropDown
from libqtile.config import EzDrag as Drag
from libqtile.config import EzKey as Key
from libqtile.config import Group, ScratchPad, Screen

import lib.widgets as mywidget
import startup
import theme
import cmd


startup_mgr = startup.StartupMgr()
startup_mgr.work()

bring_front_click = True    # bring window topside when clicking

floating_layout = layout.Floating(**theme.layout_floating)
layouts = [
    layout.Columns(
        insert_position=1,
        **theme.layout_column),
    layout.Floating(**theme.layout_floating),
]

groups = [
    Group("home", label=" Earth", layouts=[layouts[0]], spawn=[env.bin_term]),
    Group("yard", label=" Planet", layouts=[
          layouts[0]], spawn=[env.bin_browser]),
    Group("stash", label=" Stash", layouts=[layouts[0]]),
    Group("float", label=" Float", layouts=[layouts[1]]),
    Group("ghost", label=" Ghost", layouts=[layouts[0]]),
    ScratchPad("scratchpad", [
        DropDown(
            name="term",
            cmd=env.bin_term,
            **theme.dropdown),
    ]),
]

widget_defaults = theme.widget_defaults
screens = [
    Screen(left=bar.Bar([], 500, opacity=0), top=bar.Bar([
        mywidget.ImageButton(
            filename="~/.config/qtile/assets/arch-logo.svg",
            margin_x=2,
            margin_y=2,
            execute=["jgmenu_run"],
        ),
        widget.GroupBox(
            visible_groups=["home", "yard", "stash", "float"],
            **theme.groupbox),
        widget.Prompt(
            ignore_dups_history=True,
            **theme.prompt),
        widget.Spacer(length=10),
        mywidget.TaskList(
            title_width_method="uniform",
            highlight_method="border",
            **theme.tasklist),
        widget.Notify(**theme.notify),
        widget.Systray(icon_size=20),
        widget.Spacer(length=30),
        mywidget.Wlan(
            interface=env.nic_wlan,
            disconnected_message="",  # hide itself if disconnected
            **theme.wlan_indicator),
        mywidget.Net(
            interface=[env.nic_lan, env.nic_wlan],
            **theme.net_speed),
        mywidget.Battery(
            low_percentage=0.2,
            update_interval=7,
            **theme.battery),
        widget.Backlight(
            backlight_name=env.backlight,
            **theme.backlight),
        mywidget.Volume(**theme.volume),
        mywidget.ThermalSensor(**theme.thermalSensor),
        mywidget.Clock(
            update_interval=0.5,
            **theme.datetime),
        widget.Spacer(length=10),
    ], **theme.bar)),
    Screen(top=bar.Bar([
        widget.GroupBox(
            visible_groups=["home", "yard", "stash", "float", "ghost"],
            **theme.groupbox),
        mywidget.TaskList(
            title_width_method="uniform",
            highlight_method="border",
            **theme.tasklist),
        mywidget.Clock(
            update_interval=0.5,
            **theme.datetime),
        widget.Spacer(length=10),
    ], **theme.bar)),
]

keys = [
    # qtile
    Key("M-S-C-r", lazy.restart()),
    Key("M-S-C-q", lazy.shutdown()),

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

    Key("M-S-w", cmd.disable_all_floating),
    Key("M-S-n", cmd.bring_all_floating_to_front),

    # manipulate floating window
    Key("M-<Left>", lazy.window.move_floating(-30, 0, 0, 0)),
    Key("M-<Right>", lazy.window.move_floating(30, 0, 0, 0)),
    Key("M-<Up>", lazy.window.move_floating(0, -30, 0, 0)),
    Key("M-<Down>", lazy.window.move_floating(0, 30, 0, 0)),
    Key("M-S-<Left>", lazy.window.resize_floating(-30, 0, 0, 0)),
    Key("M-S-<Right>", lazy.window.resize_floating(30, 0, 0, 0)),
    Key("M-S-<Up>", lazy.window.resize_floating(0, -30, 0, 0)),
    Key("M-S-<Down>", lazy.window.resize_floating(0, 30, 0, 0)),
]
for keycode, group in zip("asdfg", ["home", "yard", "stash", "float", "ghost"]):
    keys.extend([
        Key("M-" + keycode, lazy.group[group].toscreen()),
        Key("M-C-" + keycode, lazy.window.togroup(group)),
    ])

mouse = [
    Drag("M-1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag("M-3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
]
