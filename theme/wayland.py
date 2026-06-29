# {{{ Layout and Window
layout_column = dict(
    border_width=1,
    margin_on_single=[75, 130, 100, 130],
)

layout_floating = dict(
    border_width=4,
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

groupbox = dict(
    font="monospace",
    spacing=-3,
    borderwidth=2,
    highlight_method="line",
)

tasklist = dict(
    theme_mode='preferred',
    highlight_method='block',
    fontsize=15,
    icon_size=20,
    title_width_method="uniform",
    max_title_width=250,
    spacing=15,
    margin_y=0,
    padding_x=5,
    padding_y=4,
    borderwidth=0,
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

netspeed = dict(
    font="monospace bold",
    icon_upload="",
    icon_download="",
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
