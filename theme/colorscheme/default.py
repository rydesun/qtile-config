foreground = "#0ec2c5"
foreground_soft = "#56b6c2"
foreground_hard = "#dcdfe4"
background = "#14272d"
background_blob = "#215578"
shadow = "#000000"

sudden = "#e06c75"
danger = "#b678ad"
notice = "#a5a07b"
hint = "#33a3a8"
safe = "#58b379"
major = safe
minor = "#1d677a"

layout_floating = dict(
    border_focus=background,
    border_normal=background,
)

bar = dict(
    opacity=1,
    background=background,
)

widget_defaults = dict(
    foreground=foreground,
    fontshadow=shadow,
)

menu_button = dict(
    fontshadow=None,
)

groupbox = dict(
    background=minor,
    highlight_color=minor,
    inactive=background,
    active=major,
    this_current_screen_border=major,
    this_screen_border=major,
    other_current_screen_border=background,
    other_screen_border=background,
    urgent_border=sudden,
)

tasklist = dict(
    markup_floating_color=foreground_soft,
    markup_maximized_color=foreground_soft,
    markup_minimized_color=foreground_soft,
    foreground=foreground_hard,
    border=major,
    unfocused_border=minor,
    urgent_border=sudden,
)

chord = dict()

netspeed = dict()

battery = dict(
    foreground=safe,
    foreground_discharge=notice,
    foreground_low=danger,
)

kdeconnect = dict(
    foreground=hint,
    foreground_discharge=hint,
    foreground_low=danger,
)

backlight = dict()

volume = dict()

thermalSensor = dict(
    foreground=safe,
    foreground_alert=danger,
)

clock = dict()

wallpaper = dict(
    fontshadow=None,
)
