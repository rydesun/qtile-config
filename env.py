import os
import subprocess

from libqtile import hook

from lib.theme import WallpaperManager

bin_browser = os.environ.get("BROWSER")
bin_term = "alacritty"
bin_hint_window = "nc_flash_window"

backlight = "intel_backlight"
nic_lan = "enp3s0"
nic_wlan = "wlp2s0"

wallpaper_dir = os.path.expanduser("~/Userdata/Pictures/wallpapers/")
default_wallpaper_manager = WallpaperManager(wallpaper_dir)

# init start
hook.subscribe.startup_once(default_wallpaper_manager.random_set_wallpaper)
hook.subscribe.startup_once(lambda: subprocess.Popen(['picom']))
hook.subscribe.startup_once(lambda: subprocess.Popen(['copyq']))
hook.subscribe.startup_once(lambda: subprocess.Popen(['fcitx']))
hook.subscribe.startup_once(lambda: subprocess.Popen(['syncthing']))

# init start and restart
hook.subscribe.startup(default_wallpaper_manager.random_set_wallpaper)
