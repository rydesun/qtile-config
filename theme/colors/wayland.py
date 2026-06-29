foreground = "#bbbbbb"
background = "#000000b0"

sudden = "#d8747c"
major = foreground
minor = "#1d677a"

layout_column = dict(
    border_focus="#000000e0",
    border_normal="#000000e0",
    border_focus_stack="#000000e0",
    border_normal_stack="#000000e0",
)

fake_shadow = ["#00000010", "#0000001b", "00000026", "00000031"]
layout_floating = dict(
    border_focus=fake_shadow,
    border_normal=fake_shadow,
)

bar = dict(
    background=background,
)

widget_defaults = dict(
    foreground=foreground,
)

groupbox = dict(
    highlight_color="#00000000",
    active=major,
    inactive=minor,
    this_current_screen_border=major,
    this_screen_border=major,
    other_current_screen_border=background,
    other_screen_border=background,
    urgent_border=sudden,
)

tasklist = dict(
    markup_floating_color=foreground,
    markup_maximized_color=foreground,
    markup_minimized_color=foreground,
    foreground=foreground,
    border=["#c0c0c0a0", "#a0a0a060"] + ["#a0a0a050"] * 9,
    unfocused_border=["#a0a0a0a0"] + ["#80808050"] * 2 + ["#20202050"] * 8,
    urgent_border=["#f0b0e0a0", "#e0a0d060"] + ["#c090a050"] * 9,
)

clock = dict()
