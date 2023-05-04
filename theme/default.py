# {{{ Layout and Window
layout_column = dict(
    border_width=0,
    margin_on_single=[60, 200, 80, 200],
)

layout_floating = dict(
    border_width=0,
)

dropdown_window = dict(
    x=0.2,
    y=0.1,
    width=0.6,
    height=0.7,
)
# }}}

# {{{ Bar and Widget
bar = dict(
    size=32,
)

widget_defaults = dict(
    font="sans",
    fontsize=16,
)

menu_button = dict(
    margin_x=3,
    margin_y=3,
    extra_offsety=-1,
)

groupbox = dict(
    font="monospace",
    margin_x=8,
    spacing=3,
    borderwidth=2,
    highlight_method="line",
)

tasklist = dict(
    theme_mode='preferred',
    fontsize=14,
    icon_size=16,
    title_width_method="uniform",
    max_title_width=200,
    spacing=12,
    margin_y=0,
    padding_x=8,
    icon_offset_x=0,
    icon_offset_y=2,
    borderwidth=2,
    markup_floating="  <span foreground='{color}'></span>   {{}}",
    markup_maximized="  <span foreground='{color}'></span>   {{}}",
    markup_minimized="  <span foreground='{color}'></span>   {{}}",
)

systray = dict(
    icon_size=22,
)

netspeed = dict(
    font="monospace",
    icon_upload="",
    icon_download="",
    extra_offsety=0.3,
)

battery = dict(
    format="{extra_icon} {icon}{percent: .0f}",
    icon_charge="",
    icon_discharge="",
    icon_plug="",
    icon_full_energy="",
    icon_high_energy="",
    icon_half_energy="",
    icon_low_energy="",
    icon_empty_energy="",
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
    icon=" ",
    icon_mute="󰖁 ",
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
    extra_offsety=-1,
)

wallpaper = dict(
    fmt="󰊠",
    fontsize=18,
    extra_offsety=-1.8,
)
# }}}

# vim:fdm=marker
