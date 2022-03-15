# Rename this file to env.py

from libqtile.config import Match

#################
# External assets
#################

wallpaper_main_dir = "~/Userdata/Pictures/wallpapers/"
wallpaper_other_dir = wallpaper_main_dir

# Arch Linux: Run `sudo pacman -S archlinux-artwork`
logo_file = "/usr/share/archlinux/icons/archlinux-icon-crystal-256.svg"
logo_text = "<span foreground='#dcdfe4'>arch</span>\
<span foreground='#3ba4d8'>linux</span>"

###################
# External programs
###################

cmd_term = ["kitty", "--single-instance"]
cmd_term_alter = ["kitty"]
cmd_browser = ["firefox"]
cmd_lock_screen = ["loginctl", "lock-session"]
cmd_menu = ["jgmenu_run"]
cmd_launcher = ["rofi", "-show", "combi"]
cmd_password_manager = ["rofi-rbw"]
cmd_screenshot = ["flameshot", "screen"]
cmd_screenshot_select = ["flameshot", "gui"]
cmd_screenshot_window = ["scrot", "-u"]
cmd_note = ["kitty", "-e", "joplin"]
cmd_backlight_decrease = ["brightnessctl", "s", "1%-"]
cmd_backlight_increase = ["brightnessctl", "s", "+1%"]
cmd_volume_toggle = ["pactl", "set-sink-mute", "0", "toggle"]
cmd_volume_decrease = ["pactl", "set-sink-volume", "0", "-2%"]
cmd_volume_increase = ["pactl", "set-sink-volume", "0", "+2%"]

#################
# Hardware device
#################

total_screens = 2
main_screen_scale = 1
other_screen_scale = 1

# Backlight device name.
# Run `ls /sys/class/backlight`
# Or run `brightnessctl`
dev_backlight = "amdgpu_bl0"

# Thermal sensor name.
# Run `tail /sys/class/hwmon/hwmon*/name`
# Or run `sensors`
dev_thermal = "acpitz"

# Network device names.
# Run `ls /sys/class/net`
# Or run `nmcli device`
dev_nic = ["wlp1s0", "enp2s0"]

# If you have connected your phone to kdeconnect,
# set the device ID to show its battery status.
# Run `kdeconnect-cli --list-devices`
dev_kdeconnect = None
# dev_kdeconnect = "eeeeeeeeeeeeeeee"

#########################
# layout and window rules
#########################

# The window matching these rules will float.
float_rules = [
    Match(wm_class="firefox", role="Organizer"),
    Match(wm_class="firefox", role="page-info"),
    Match(wm_class="firefox", role="About"),
    Match(wm_class="lxqt-config"),
    Match(wm_class="pinentry-qt"),
    Match(wm_class="scrcpy"),
    Match(wm_class="Steam"),
]

# Set the appearance of floating windows.
float_config = [
    {"match": Match(wm_class="kitty"), "border_width": 2},
]
