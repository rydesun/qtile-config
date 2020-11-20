from libqtile import bar, layout, widget
from libqtile.command import lazy
from libqtile.config import DropDown
from libqtile.config import EzDrag as Drag
from libqtile.config import EzKey as Key
from libqtile.config import Key as SpecKey
from libqtile.config import Group, ScratchPad, Screen

from layout.columns import Columns
import lib.widgets as mywidget
import startup
import theme
import cmd
import env


startup_mgr = startup.StartupMgr(env)
startup_mgr.subreaper()
startup_mgr.work()

bring_front_click = True    # bring window topside when clicking

floating_layout = layout.Floating(**theme.layout_floating)
layouts = [
    Columns(
        insert_position=1,
        **theme.layout_column),
    layout.Floating(**theme.layout_floating),
]

groups = [
    Group("a", label="⬤", layouts=[layouts[0]], spawn=[env.bin_term]),
    Group("s", label="⬤", layouts=[
          layouts[0]], spawn=[env.bin_browser]),
    Group("d", label="⬤", layouts=[layouts[0]]),
    Group("f", label="⬤", layouts=[layouts[1]]),
    Group("g", label="⬤", layouts=[layouts[0]]),
    ScratchPad("scratchpad", [
        DropDown(
            name="term",
            cmd=env.bin_term,
            **theme.dropdown),
    ]),
]

widget_defaults = theme.widget_defaults
screens = [
    Screen(top=bar.Bar([
        mywidget.ImageButton(
            filename="/usr/share/archlinux/icons/archlinux-icon-crystal-256.svg",
            margin_x=3,
            margin_y=3,
            execute=["jgmenu_run"],
        ),
        mywidget.TextBox(
            text="arch<span foreground='#3ba4d8'>linux</span>",
            extra_offsetx = -7,
            extra_offsety = -1.5,
            execute=["jgmenu_run"],
        ),
        widget.GroupBox(
            visible_groups=["a", "s", "d", "f"],
            disable_drag=True,
            **theme.groupbox),
        widget.Prompt(
            ignore_dups_history=True,
            **theme.prompt),
        widget.Spacer(length=10),
        mywidget.TaskList(
            title_width_method="uniform",
            **theme.tasklist),
        widget.Notify(**theme.notify),
        widget.Systray(icon_size=22),
        widget.Spacer(length=20),
        mywidget.Net(
            interface=[env.nic_wlan],
            **theme.net_speed),
        mywidget.Battery(
            low_percentage=0.2,
            update_interval=7,
            **theme.battery),
        mywidget.Backlight(
            backlight_name=env.backlight,
            change_command='brightnessctl s {0}',
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
            visible_groups=["a", "s", "d", "f", "g"],
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

    Key("M-r", lazy.spawn(["rofi", "-show", "combi"])),
    Key("M-t", lazy.spawn(["input-box"])),          # chinese input box
    Key("M-q", lazy.window.toggle_fullscreen()),    # toggle window fullscreen
    Key("M-w", lazy.window.toggle_floating()),      # toggle window floating
    Key("M-x", lazy.window.kill()),                 # close window

    Key("M-S-w", cmd.disable_all_floating),
    Key("M-S-n", cmd.bring_all_floating_to_front),

    # manipulate floating window
    Key("M-<Left>", lazy.window.move_floating(-30, 0)),
    Key("M-<Right>", lazy.window.move_floating(30, 0)),
    Key("M-<Up>", lazy.window.move_floating(0, -30)),
    Key("M-<Down>", lazy.window.move_floating(0, 30)),
    Key("M-S-<Left>", lazy.window.resize_floating(-30, 0)),
    Key("M-S-<Right>", lazy.window.resize_floating(30, 0)),
    Key("M-S-<Up>", lazy.window.resize_floating(0, -30)),
    Key("M-S-<Down>", lazy.window.resize_floating(0, 30)),

    SpecKey([], "XF86AudioMute", lazy.spawn(["amixer", "-q", "sset", "Master", "toggle"])),
    SpecKey([], "XF86AudioLowerVolume", lazy.spawn(["amixer", "-q", "sset", "Master", "1%-"])),
    SpecKey([], "XF86AudioRaiseVolume", lazy.spawn(["amixer", "-q", "sset", "Master", "1%+"])),
    SpecKey([], "XF86MonBrightnessUp", lazy.spawn(["brightnessctl", "s", "+1%"])),
    SpecKey([], "XF86MonBrightnessDown", lazy.spawn(["brightnessctl", "s", "1%-"])),
]
for k in "asdfg":
    keys.extend([
        Key("M-" + k, lazy.group[k].toscreen()),
        Key("M-C-" + k, lazy.window.togroup(k)),
    ])

mouse = [
    Drag("M-1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag("M-3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
]
