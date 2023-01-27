# Rename this file to env.py

import os

from libqtile.config import Match

# Feel free to edit, comment or delete these lines,
# which will disable the relevant widgets.

# {{{ External assets
# Arch Linux: Run `sudo pacman -S archlinux-wallpaper`
wallpaper_main_default = "/usr/share/backgrounds/archlinux/small.png"
# random select one from dir if default is omitted
wallpaper_main_dir = "/usr/share/backgrounds/archlinux/"

# Other screens
wallpaper_other_default = "/usr/share/backgrounds/archlinux/simple.png"
wallpaper_other_dir = "/usr/share/backgrounds/archlinux/"

# Arch Linux: Run `sudo pacman -S archlinux-artwork`
logo_file = "/usr/share/archlinux/icons/archlinux-icon-crystal-256.svg"
logo_text = "<span foreground='#dcdfe4'>arch</span><span foreground='#3ba4d8'>linux</span>"
# }}}

# {{{ External programs
cmd_term = ["kitty", "--single-instance",
            "--instance-group", os.getenv("XDG_VTNR", "default")]
cmd_browser = ["firefox"]
cmd_menu = ["jgmenu_run"]
cmd_launcher = ["rofi", "-show", "combi"]

cmd_screenshot_select = ["spectacle", "--region"]
cmd_screenshot_window = ["spectacle", "--activewindow"]
cmd_screenshot_fullscreen = ["spectacle", "--fullscreen"]

cmd_network = ["wireshark"]

cmd_backlight_decrease = ["brightnessctl", "s", "1%-"]
cmd_backlight_increase = ["brightnessctl", "s", "+1%"]
cmd_volume_toggle = ["pactl", "set-sink-mute", "0", "toggle"]
cmd_volume_decrease = ["pactl", "set-sink-volume", "0", "-2%"]
cmd_volume_increase = ["pactl", "set-sink-volume", "0", "+2%"]
cmd_volume_control = ["pavucontrol-qt"]

dropdowns = [
    {"key": "t", "name": "term", "cmd": ["kitty"]},
]

cmd_bindings = [
    {"key": "e", "cmd": ["dolphin"]},
    {"key": "p", "cmd": ["loginctl", "lock-session"]},
]
# }}}

# {{{ Hardware devices
total_screens = 2

# Backlight device name.
# Run `ls /sys/class/backlight`
# Or run `brightnessctl`
dev_backlight = "amdgpu_bl0"

# Run `pactl list | grep node.name`
# Such as name that start with bluez represents bluetooth headphone
dev_headphone_sinks = ["bluez_output.XX_XX_XX_XX_XX_XX.a2dp-sink"]

# Thermal sensor name.
# Run `tail /sys/class/hwmon/hwmon*/name`
# Or run `sensors`
dev_thermal = "acpitz"

# Network device names. Glob supported.
# Run `ls /sys/class/net`
# Or run `nmcli device`
dev_nic = ["enp*", "wlp*"]

# If you have connected your phone to kdeconnect,
# set the device ID to show its battery status.
# Run `kdeconnect-cli --list-devices`
dev_kdeconnect = None
# dev_kdeconnect = "eeeeeeeeeeeeeeee"
# }}}

# {{{ Groups
groups = [
    {"key": "a", "bind_window": {
        "cmd": cmd_term,
        "match": Match(wm_class="kitty"),
    }},
    {"key": "s", "bind_window": {
        "cmd": cmd_browser,
        "match": Match(wm_class="firefox", role="browser"),
    }},
    {"key": "d", "bind_window": {}},
    {"key": "f", "bind_window": {}},
]
# }}}

# {{{ Layout and window rules
# The window matching these rules will float.
float_rules = [
    Match(wm_class="firefox", role="Organizer"),
    Match(wm_class="firefox", role="page-info"),
    Match(wm_class="firefox", role="About"),
    Match(wm_class="firefox", role="toolbox"),
    Match(wm_class="firefox", role="Toplevel"),
    Match(wm_class="lxqt-config"),
    Match(wm_class="pinentry-qt"),
    Match(wm_class="scrcpy"),
    Match(wm_class="Steam"),
]

# Set the appearance of floating windows.
float_config = [
    {"match": Match(wm_class="kitty"), "border_width": 0},
]
# }}}

# vim:fdm=marker
