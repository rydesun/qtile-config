import subprocess
from libqtile.config import Screen, Group, EzKey as Key, EzDrag as Drag, EzClick as Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook

# 重写默认widget的功能
import widget_rewrite
widget.Net.poll = widget_rewrite.new_net_poll
widget.Net.get_stats = widget_rewrite.new_net_get_stats
widget.Backlight.poll = widget_rewrite.new_backlight_poll
widget.Battery.update = widget_rewrite.new_battery_update

# 在此设置自己的默认浏览器和虚拟终端
BROWSER = "waterfox"
TERMINAL = "st"

groups = [
    Group("a", spawn=[TERMINAL]),
    Group("s", spawn=[BROWSER]),
    Group("d"),
    Group("f"),
]

layouts = [
    layout.Columns(border_width=0),
    layout.Columns(border_width=2, border_focus='427b58', border_normal='282828'),
]

widget_defaults = {'font': 'Droid Sans Mono', 'padding': 0, 'foreground': 'd3869b'}
widget_sep_defaults = {'padding': 14, 'linewidth': 2, 'foreground': '928374'}

# 在此添加widgets
screens = [
    Screen(top=bar.Bar([
        widget.GroupBox(
            center_aligned=True, visible_groups=["a", "s", "d"],
            highlight_method='block', this_current_screen_border='427b58',
            active="ebdbb2", inactive="3c3836", fontsize=14, borderwidth=3, rounded=False),
        widget.Prompt(record_history=False, prompt=">>> ", fontsize=12),
        widget.Notify(),
        widget.Spacer(),
        widget.Net(),
        widget.Sep(**widget_sep_defaults),
        widget.Battery(
            battery_name='BAT1', format='{char}{percent:2.0%}',
            charge_char='\uf137', discharge_char='\uf136'),
        widget.Sep(**widget_sep_defaults),
        widget.TextBox(text='\uf3b0'),
        widget.Backlight(backlight_name='intel_backlight'),
        widget.Sep(**widget_sep_defaults),
        widget.TextBox(text='\uf3ba'),
        widget.Volume(),
        widget.Sep(**widget_sep_defaults),
        widget.Systray(icon_size=15),
        widget.Clock(format='%Y-%m-%d %A %H:%M:%S ', foreground='ebdbb2', update_interval=0.5, padding=5),
        ], 17, background=["1d2021"])),
]

# 按键映射
keys = [
    Key("<XF86MonBrightnessDown>", lazy.spawn('xbacklight -dec 1')),
    Key("<XF86MonBrightnessUp>", lazy.spawn('xbacklight -inc 1')),
    Key("<XF86AudioLowerVolume>", lazy.spawn("ponymix decrease 1")),
    Key("<XF86AudioRaiseVolume>", lazy.spawn("ponymix increase 1")),
    Key("<XF86AudioMute>", lazy.spawn("ponymix toggle")),

    Key("M-S-r", lazy.restart()),
    Key("M-S-q", lazy.shutdown()),
    Key("M-<Return>", lazy.spawn(TERMINAL)),

    Key("M-<space>", lazy.next_layout()),
    Key("M-j", lazy.layout.down()),
    Key("M-k", lazy.layout.up()),
    Key("M-h", lazy.layout.left()),
    Key("M-l", lazy.layout.right()),
    Key("M-C-j", lazy.layout.shuffle_down()),
    Key("M-C-k", lazy.layout.shuffle_up()),
    Key("M-C-h", lazy.layout.shuffle_left()),
    Key("M-C-l", lazy.layout.shuffle_right()),
    Key("M-S-j", lazy.layout.grow_down()),
    Key("M-S-k", lazy.layout.grow_up()),
    Key("M-S-h", lazy.layout.grow_left()),
    Key("M-S-l", lazy.layout.grow_right()),
    Key("M-n", lazy.layout.normalize()),
    Key("M-<Tab>", lazy.layout.toggle_split()),

    Key("M-r", lazy.spawncmd()),
    Key("M-q", lazy.window.toggle_fullscreen()),
    Key("M-z", lazy.window.toggle_floating()),
    Key("M-x", lazy.window.kill()),
]
for i, j in zip(groups, "asdf"):
    keys.extend([
        Key("M-" + j, lazy.group[i.name].toscreen()),
        Key("M-C-" + j, lazy.window.togroup(i.name)),
    ])

# 鼠标映射
mouse = [
    Drag("M-1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag("M-3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click("M-2", lazy.window.toggle_floating()),
]

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating()
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "LG3D"

# 设置默认自启程序
@hook.subscribe.startup_once
def autostart():
    subprocess.Popen(['fcitx'])
