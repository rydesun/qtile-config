# Rename this file to env.py

import os

from libqtile.config import Match

wallpaper_dir = os.path.expanduser("~/Userdata/Pictures/wallpapers/")

logo_file = "/usr/share/archlinux/icons/archlinux-icon-crystal-256.svg"
logo_text = "arch<span foreground='#3ba4d8'>linux</span>"

sh_browser = "firefox"
sh_term = "kitty --single-instance"

cmd_locker = ["xss-lock", "--", "betterlockscreen", "-l"]
cmd_lock_screen = ["loginctl", "lock-session"]
cmd_term = ["kitty"]
cmd_menu = ["jgmenu_run"]
cmd_launcher = ["rofi", "-show", "combi"]
cmd_password_manager = ["rofi-rbw"]
cmd_screenshot = ["flameshot", "screen"]
cmd_screenshot_select = ["flameshot", "gui"]
cmd_screenshot_window = ["scrot", "-u"]
cmd_note = ["kitty", "-e", "joplin"]
cmd_wallpaper = ["feh", "--bg-fill", "--no-fehbg"]
cmd_backlight_decrease = ["brightnessctl", "s", "1%-"]
cmd_backlight_increase = ["brightnessctl", "s", "+1%"]
cmd_volume_toggle = ["amixer", "-q", "sset", "Master", "toggle"]
cmd_volume_decrease = ["amixer", "-q", "sset", "Master", "1%-"]
cmd_volume_increase = ["amixer", "-q", "sset", "Master", "1%+"]

dev_backlight = "amdgpu_bl0"
dev_thermal = "acpitz"
dev_nic = ["wlp1s0", "enp2s0"]
dev_kdeconnect = "eeeeeeeeeeeeeeee"

float_rules = [
    Match(wm_class="firefox", role="Organizer"),
    Match(wm_class="firefox", role="page-info"),
    Match(wm_class="firefox", role="About"),
    Match(wm_class="Steam"),
    Match(wm_class="pinentry-qt"),
]

float_config = [
    {"match": Match(wm_class="kitty"), "border_width": 2},
]
