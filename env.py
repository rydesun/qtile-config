import os

bin_browser = os.environ.get("BROWSER")
bin_term = "alacritty"
bin_hint_window = "nc_flash_window"

backlight = "intel_backlight"
nic_lan = "enp3s0"
nic_wlan = "wlp2s0"

wallpaper_dir = os.path.expanduser("~/Userdata/Pictures/wallpapers/")

boot_cmds = [['picom'], ['copyq'], ['fcitx'], ['nm-applet']]
