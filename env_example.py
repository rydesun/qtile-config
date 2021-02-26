# Rename this file to env.py

import os

from libqtile.config import Match


wallpaper_dir = os.path.expanduser("~/Userdata/Pictures/wallpapers/")

logo_file = "/usr/share/archlinux/icons/archlinux-icon-crystal-256.svg"
logo_text = "arch<span foreground='#3ba4d8'>linux</span>"

bin_browser = "firefox"
bin_term = "alacritty"
cmd_menu = ["jgmenu_run"]
cmd_launcher = ["rofi", "-show", "combi"]
cmd_note = ["alacritty", "-e", "joplin"]
cmd_wallpaper = ["hsetroot", "-cover"]
cmd_backlight = "brightnessctl s {}"
cmd_backlight_decrease = ["brightnessctl", "s", "1%-"]
cmd_backlight_increase = ["brightnessctl", "s", "+1%"]
cmd_volume_toggle = ["amixer", "-q", "sset", "Master", "toggle"]
cmd_volume_decrease = ["amixer", "-q", "sset", "Master", "1%-"]
cmd_volume_increase = ["amixer", "-q", "sset", "Master", "1%+"]

dev_backlight = "amdgpu_bl0"
dev_nic = ["wlp1s0", "enp2s0"]
dev_kdeconnect = "eeeeeeeeeeeeeeee"

float_rules = [
    Match(wm_class="fcitx-config-gtk3"),
    Match(wm_class="Lxappearance"),
    Match(wm_class="firefox", role="Organizer"),
    Match(wm_class="firefox", role="page-info"),
]
float_borders = [
    {"match": Match(wm_class="Alacritty"), "border_width": 2},
]
