# Qtile Configuration

Essential dependency packages to install

```bash
sudo pacman -S --needed python-dbus-next python-psutil python-pyxdg
# Install upower if have a battery
sudo pacman -S --needed upower
```

As for icon font, you need nerd font or at least one font
that has been patched

```bash
sudo pacman -S --needed ttf-nerd-fonts-symbols
```

More resources

```bash
# archlinux logo (from AUR)
pikaur archlinux-artwork
# archlinux wallpapers
sudo pacman -S --needed archlinux-wallpaper
```

Optional patch

```bash
sudo patch /usr/lib/python3.*/site-packages/libqtile/drawer.py top_line.patch
```

## Customization

First you should refer to `env_example.py` for creating the `env.py`,
which is mainly about hardware devices and unique system environment.
It's yours, not mine. 😃
Although the lack of `env.py` does not cause qtile to crash on startup,
it's better to create one.

Most of the appearance settings are stored in `theme/`.

`control.py` is about keymappings and shortcuts.

`bar.py` focus on widgets on the bar.

## Companion

Highly recommended companion applications

- picom — X compositor
- dunst — Notification daemon
- rofi — Application launcher

Systray icon

- papirus-icon-theme
