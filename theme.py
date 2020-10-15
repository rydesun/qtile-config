# colorscheme: Material
color0 = "263238"; color8  = "37474f" # black
color1 = "ff9800"; color9  = "ffa74d" # red
color2 = "8bc34a"; color10 = "9ccc65" # green
color3 = "ffc107"; color11 = "ffa000" # yellow
color4 = "03a9f4"; color12 = "81d4fa" # blue
color5 = "e91e63"; color13 = "ad1457" # magenta
color6 = "009688"; color14 = "26a69a" # cyan
color7 = "cfd8dc"; color15 = "eceff1" # white
# extra colorscheme
color_foreground = color15
color_background = color0
color_green = "427b58"; color_light_green = "cdf3a9"
color_light_yellow = "ebdbb2"
color_dark_blue = "445582"
color_pink = "b68992"
# font
font_sans = "sans"
font_mono = "monospace"


# layout
_column_border_width = 0
_column_window_margin = 10
_float_border_width = 0
# dropdown
_drowndown_x = 0.2
_drowndown_y = 0
_drowndown_width = 0.8
_drowndown_height = 0.8
# bar
_bar_size = 34
_bar_font = font_sans
_bar_fontsize = 16
_bar_fontsize_has_outline = 14
_bar_color_foreground = color_foreground
_bar_color_background = color_background
# widget: groupbox
_groupbox_font      = font_sans
_groupbox_fontsize  = _bar_fontsize_has_outline
_groupbox_margin    = 15
_groupbox_spacing   = 9
_groupbox_highlight_method = "block"
_groupbox_color_background         = color8
_groupbox_color_foreground_inative = color_foreground
_groupbox_color_foreground_active  = color_light_yellow
_groupbox_color_normal       = color_green
_groupbox_color_normal_other = color_dark_blue
_groupbox_color_urgent       = color_pink
# widget: prompt
_prompt_font  = font_mono
_prompt_icon  = " "
_prompt_color = color2
# widget: tasklist
_tasklist_max_width = 200
_tasklist_spacing   = 12
_tasklist_fontsize  = _bar_fontsize_has_outline
_tasklist_icon_size = 20
_tasklist_margin_y  = 0
_tasklist_padding_y = 4
_tasklist_icon_offset_x = 0
_tasklist_icon_offset_y = -1
_tasklist_hint_floating  = " "
_tasklist_hint_maximized = " "
_tasklist_hint_minimized = " "
_tasklist_borderwidth = 2
_tasklist_color_border_focused   = color10
_tasklist_color_border_unfocused = color14
_tasklist_color_border_urgent    = color1
# widget: notify
_notify_normal = color_light_yellow
_notify_low    = color_foreground
_notify_urgent = color1
# widget: net
_net_wifi_icon     = ""
_net_download_icon = ""
_net_upload_icon   = ""
_net_speed_font    = font_mono
_net_color         = color4
# widget: sensor
_sensor_color       = color6
_sensor_color_warn  = color3
_sensor_color_alert = color5
_sensor_battery_plug_icon = ""
_sensor_battery_charge_icon = ""
_sensor_battery_discharge_icon = ""
_sensor_battery_full_energy_icon = ""
_sensor_battery_high_energy_icon = ""
_sensor_battery_half_energy_icon = ""
_sensor_battery_low_energy_icon = ""
_sensor_battery_empty_energy_icon = ""
_sensor_backlight_icon = ""
# widget: calendar and clock
_date_icon      = ""
_time_icon      = ""
_datetime_color = color2


# wallpaper
wallpaper_color = "#707070"
# layout: floating
layout_floating = dict(
    border_width=_float_border_width,
)
# layout: column
layout_column = dict(
    border_width=_column_border_width,
    margin=_column_window_margin,
)
# dropdown
dropdown = dict(
    x=_drowndown_x,
    y=_drowndown_y,
    width=_drowndown_width,
    height=_drowndown_height,
)
# widget
widget_defaults = dict(
    font=_bar_font,
    fontsize=_bar_fontsize,
    foreground=_bar_color_foreground,
)
bar = dict(
    size=_bar_size,
    background=_bar_color_background,
    opacity=0.95,
)
groupbox = dict(
    font=_groupbox_font,
    fontsize=_groupbox_fontsize,
    background=_groupbox_color_background,
    margin_x=_groupbox_margin,
    spacing=_groupbox_spacing,
    active=_groupbox_color_foreground_active,
    inactive=_groupbox_color_foreground_inative,

    highlight_method=_groupbox_highlight_method,
    this_current_screen_border=_groupbox_color_normal,
    this_screen_border=_groupbox_color_normal,
    other_current_screen_border=_groupbox_color_normal_other,
    other_screen_border=_groupbox_color_normal_other,
    urgent_border=_groupbox_color_urgent,
)
prompt = dict(
    font=_prompt_font,
    prompt=_prompt_icon,
    foreground=_prompt_color,
)
tasklist = dict(
    max_title_width=_tasklist_max_width,
    spacing=_tasklist_spacing,
    fontsize=_tasklist_fontsize,
    icon_size=_tasklist_icon_size,
    margin_y=_tasklist_margin_y,
    padding_y=_tasklist_padding_y,
    icon_offset_x=_tasklist_icon_offset_x,
    icon_offset_y=_tasklist_icon_offset_y,
    txt_floating=_tasklist_hint_floating,
    txt_maximized=_tasklist_hint_maximized,
    txt_minimized=_tasklist_hint_minimized,
    borderwidth=_tasklist_borderwidth,
    border=_tasklist_color_border_focused,
    unfocused_border=_tasklist_color_border_unfocused,
    urgent_border=_tasklist_color_border_urgent,
)
notify = dict(
    foreground=_notify_normal,
    foreground_low=_notify_low,
    foreground_urgent=_notify_urgent,
)
wlan_indicator = dict(
    icon=_net_wifi_icon,
    foreground=_net_color,
)
net_speed = dict(
    icon_upload=_net_upload_icon,
    icon_download=_net_download_icon,
    font=_net_speed_font,
    foreground=_net_color,
)
volume = dict(
    foreground=_sensor_color,
)
thermalSensor = dict(
    foreground=_sensor_color,
    foreground_alert=_sensor_color_alert,
)
battery = dict(
    format="{extra_icon} {icon} {percent:2.0%}",
    icon_charge=_sensor_battery_charge_icon,
    icon_discharge=_sensor_battery_discharge_icon,
    icon_plug=_sensor_battery_plug_icon,
    icon_full_energy=_sensor_battery_full_energy_icon,
    icon_high_energy=_sensor_battery_high_energy_icon,
    icon_half_energy=_sensor_battery_half_energy_icon,
    icon_low_energy=_sensor_battery_low_energy_icon,
    icon_empty_energy=_sensor_battery_empty_energy_icon,
    foreground=_sensor_color,
    foreground_discharge=_sensor_color_warn,
    foreground_low=_sensor_color_alert,
)
backlight = dict(
    format=_sensor_backlight_icon + "{percent: 2.0%}",
    foreground=_sensor_color,
)
datetime = dict(
    format="{} %H:%M:%S  {} %m-%d  ".format(_time_icon, _date_icon),
    foreground=_datetime_color,
)
