# {{{ Layout and Window
layout_column = dict(
    border_width=0,
    margin_on_single=[70, 130, 100, 130],
)

layout_floating = dict(
    border_width=0,
)

dropdown_window = dict(
    x=0.25,
    y=0.2,
    width=0.5,
    height=0.6,
    opacity=1,
)
# }}}

# {{{ Bar and Widget
bar = dict(
    size=28,
)

widget_defaults = dict(
    font="sans bold",
    fontsize=16,
)

menu_button = dict(
    margin_x=10,
    margin_y=5,
)

groupbox = dict(
    font="monospace",
    spacing=-3,
    borderwidth=2,
    highlight_method="line",
)

tasklist = dict(
    theme_mode='preferred',
    fontsize=15,
    icon_size=20,
    title_width_method="uniform",
    max_title_width=200,
    spacing=15,
    margin_y=0,
    padding_x=5,
    padding_y=4,
    markup_floating="<span foreground='{color}'></span>  {{}}",
    markup_maximized="<span foreground='{color}'></span>  {{}}",
    markup_minimized="<span foreground='{color}'>󰈉</span>  {{}}",
)

chord = dict(
    name_transform=lambda txt: "󰌌 "+({
        "Window": "窗口",
        "MoveWindow": "窗口方向",
        "Execute": "执行",
        "Player": "播放器",
        "Capture": "捕捉画面",
    }.get(txt) or txt)
)

systray = dict(
    icon_size=22,
)

netspeed = dict(
    font="monospace bold",
    icon_upload="",
    icon_download="",
)

battery = dict(
    format="{extra_icon} {icon}{percent: .0f}",
    icon_charge="",
    icon_discharge="",
    icon_plug="",
    icon_full_energy="󰁹",
    icon_high_energy="󰂀",
    icon_half_energy="󰁾",
    icon_low_energy="󰁼",
    icon_empty_energy="󰁺",
    extra_offsetx=5,
    extra_offsety=-0.7,
)

kdeconnect = dict(
    format="{extra_icon}{icon}{percent: .0f}",
    icon_charge=" ",
    icon_discharge="",
    icon_plug="",
    icon_full_energy="",
    icon_high_energy="",
    icon_half_energy="",
    icon_low_energy="",
    icon_empty_energy="",
    extra_offsetx=3,
    extra_offsety=-1.5,
)

backlight = dict(
    format="󰃠{percent: .0f}",
    extra_offsety=-1.5,
)

volume = dict(
    icon=" ",
    icon_mute=" ",
    icon_headphone="󰋎 ",
    icon_headphone_mute="󰋐 ",
    mute_text="M",
    extra_offsety=-1.5,
)

thermalSensor = dict(
    icon="󰈐 ",
    extra_offsety=-1.4,
)

clock = dict(
    format="%H:%M:%S  %m-%d  <span rise='1000' size='small'>{}</span>",
    weekday_sign=(
        "周一",
        "周二",
        "周三",
        "周四",
        "周五",
        "周六",
        "周日",
    ),
)
# }}}

# vim:fdm=marker
