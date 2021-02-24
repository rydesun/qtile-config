from libqtile import bar, widget
from libqtile.command import lazy
from libqtile.config import (DropDown, EzDrag, EzKey, Group, Key, ScratchPad,
                             Screen)

import command
import env
import themes
import widgets as mywidget
from layout.columns import Columns
from layout.floating import Floating
from startup import startup


startup()
theme = themes.ui.Theme(themes.colors.material)

floating_layout = Floating(
    float_rules=[
        *Floating.default_float_rules,
        *env.float_rules,
    ],
    border_rules=env.float_borders,
    **theme.layout_floating)
layouts = [
    Columns(
        insert_position=1,
        **theme.layout_column),
    Floating(**theme.layout_floating),
]

_groups = [
    Group("a", label="⬤", layouts=[layouts[0]], spawn=[env.bin_term]),
    Group("s", label="⬤", layouts=[layouts[0]], spawn=[env.bin_browser]),
    Group("d", label="⬤", layouts=[layouts[0]]),
    Group("f", label="⬤", layouts=[layouts[1]]),
    Group("g", label="⬤", layouts=[layouts[0]]),
]
groups = _groups + [
    ScratchPad("scratchpad", [
        DropDown(
            name="term",
            cmd=env.bin_term,
            **theme.dropdown_window),
    ]),
]

widget_defaults = theme.widget_defaults
screens = [
    Screen(top=bar.Bar([
        mywidget.ImageButton(
            filename=env.logo_file,
            execute=env.cmd_menu,
        **theme.menu_button),
        mywidget.TextButton(
            text=env.logo_text,
            execute=env.cmd_menu,
        **theme.menu_text),
        widget.GroupBox(
            visible_groups=["a", "s", "d", "f"],
            disable_drag=True,
            **theme.groupbox),
        widget.Spacer(length=10),
        mywidget.TaskList(**theme.tasklist),
        widget.Systray(**theme.systray),
        widget.Spacer(length=20),
        mywidget.Kdeconnect(
            low_percentage=0.2,
            update_interval=7,
            dev_id=env.dev_kdeconnect,
            **theme.kdeconnect,
        ),
        mywidget.Net(
            interface=env.dev_nic,
            **theme.netspeed),
        mywidget.Battery(
            low_percentage=0.2,
            update_interval=7,
            **theme.battery),
        mywidget.Backlight(
            backlight_name=env.dev_backlight,
            command_increase=env.cmd_backlight_increase,
            command_decrease=env.cmd_backlight_decrease,
            **theme.backlight),
        mywidget.Volume(
            mute_command=env.cmd_volume_toggle,
            volume_up_command=env.cmd_volume_increase,
            volume_down_command=env.cmd_volume_decrease,
            **theme.volume),
        mywidget.ThermalSensor(**theme.thermalSensor),
        mywidget.Clock(
            update_interval=0.5,
            **theme.clock),
        mywidget.Wallpaper(
            random_selection=True,
            directory=env.wallpaper_dir,
            wallpaper_command=env.cmd_wallpaper,
            **theme.wallpaper),
        widget.Spacer(length=10),
    ], **theme.bar)),
    Screen(top=bar.Bar([
        widget.GroupBox(
            visible_groups=["a", "s", "d", "f", "g"],
            **theme.groupbox),
        mywidget.TaskList(**theme.tasklist),
        mywidget.Clock(
            update_interval=0.5,
            **theme.clock),
        widget.Spacer(length=10),
    ], **theme.bar)),
]

keys = [
    # qtile
    EzKey("M-S-C-r", lazy.restart()),
    EzKey("M-S-C-q", lazy.shutdown()),

    # terminal emulator
    EzKey("M-<Return>", lazy.spawn(env.bin_term)),
    EzKey('M-i', lazy.group['scratchpad'].dropdown_toggle('term')),

    # toggle sidebar
    EzKey("M-<space>", lazy.hide_show_bar("left")),
    # window focus
    EzKey("M-j", lazy.layout.down()),
    EzKey("M-k", lazy.layout.up()),
    EzKey("M-h", lazy.layout.left()),
    EzKey("M-l", lazy.layout.right()),
    # window shift
    EzKey("M-C-j", lazy.layout.shuffle_down()),
    EzKey("M-C-k", lazy.layout.shuffle_up()),
    EzKey("M-C-h", lazy.layout.shuffle_left()),
    EzKey("M-C-l", lazy.layout.shuffle_right()),
    # window resize
    EzKey("M-S-j", lazy.layout.grow_down()),
    EzKey("M-S-k", lazy.layout.grow_up()),
    EzKey("M-S-h", lazy.layout.grow_left()),
    EzKey("M-S-l", lazy.layout.grow_right()),
    EzKey("M-n", lazy.layout.normalize()),            # normalize window size
    # toggle between stack and split
    EzKey("M-<Tab>", lazy.layout.toggle_split()),

    EzKey("M-r", lazy.spawn(env.cmd_launcher)),
    EzKey("M-t", lazy.spawn(["input-box"])),          # Chinese input box
    EzKey("M-q", lazy.window.toggle_fullscreen()),    # toggle window fullscreen
    EzKey("M-w", lazy.window.toggle_floating()),      # toggle window floating
    EzKey("M-x", lazy.window.kill()),                 # close window

    EzKey("M-S-w", command.disable_all_floating),
    EzKey("M-S-n", command.bring_all_floating_to_front),

    # manipulate floating window
    EzKey("M-<Left>", lazy.window.move_floating(-30, 0)),
    EzKey("M-<Right>", lazy.window.move_floating(30, 0)),
    EzKey("M-<Up>", lazy.window.move_floating(0, -30)),
    EzKey("M-<Down>", lazy.window.move_floating(0, 30)),
    EzKey("M-S-<Left>", lazy.window.resize_floating(-30, 0)),
    EzKey("M-S-<Right>", lazy.window.resize_floating(30, 0)),
    EzKey("M-S-<Up>", lazy.window.resize_floating(0, -30)),
    EzKey("M-S-<Down>", lazy.window.resize_floating(0, 30)),

    Key([], "XF86AudioMute", lazy.spawn(env.cmd_volume_toggle)),
    Key([], "XF86AudioLowerVolume", lazy.spawn(env.cmd_volume_decrease)),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(env.cmd_volume_increase)),
    Key([], "XF86MonBrightnessUp", lazy.spawn(env.cmd_backlight_increase)),
    Key([], "XF86MonBrightnessDown",
            lazy.spawn(env.cmd_backlight_decrease)),
]
for i in _groups:
    keys.extend([
        EzKey("M-" + i.name, lazy.group[i.name].toscreen()),
        EzKey("M-C-" + i.name, lazy.window.togroup(i.name)),
    ])

mouse = [
    EzDrag("M-1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    EzDrag("M-3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
]

bring_front_click = True    # bring window topside when clicking
