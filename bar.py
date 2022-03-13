from libqtile import bar, qtile
from libqtile import widget as qtile_widget
from libqtile.command import lazy

import widget as local_widget


class Bar:
    def __init__(self, env):
        self.env = env

    def main_bar(self, theme):
        return bar.Bar(list(filter(lambda w: w is not None, (
            local_widget.Box(
                image_path=self.env.logo_file,
                text=self.env.logo_text,
                mouse_callbacks={
                    "Button1": lazy.spawn(self.env.cmd_menu),
                },
                **theme.menu_button)
            if getattr(self.env, "logo_file", None)
            or getattr(self.env, "logo_text", None)
            else None,

            qtile_widget.GroupBox(
                visible_groups=["a", "s", "d", "f"],
                disable_drag=True,
                **theme.groupbox),

            qtile_widget.Spacer(length=10),

            local_widget.TaskList(**theme.tasklist),

            qtile_widget.Systray(**theme.systray)
            if qtile.core.name == "x11" else None,

            qtile_widget.Spacer(length=20),

            local_widget.Net(
                interface=self.env.dev_nic,
                **theme.netspeed)
            if getattr(self.env, "dev_nic", None)
            else None,

            local_widget.Battery(
                low_percentage=0.2,
                update_interval=7,
                **theme.battery),

            local_widget.Kdeconnect(
                low_percentage=0.2,
                update_interval=7,
                dev_id=self.env.dev_kdeconnect,
                **theme.kdeconnect)
            if getattr(self.env, "dev_kdeconnect", None)
            else None,

            local_widget.Backlight(
                backlight_name=self.env.dev_backlight,
                mouse_callbacks={
                    "Button4": lazy.spawn(self.env.cmd_backlight_increase),
                    "Button5": lazy.spawn(self.env.cmd_backlight_decrease),
                },
                **theme.backlight)
            if getattr(self.env, "dev_backlight", None)
            else None,

            local_widget.PulseVolume(
                **theme.volume),

            local_widget.ThermalSensor(
                dev_name=self.env.dev_thermal,
                **theme.thermalSensor)
            if getattr(self.env, "dev_thermal", None)
            else None,

            local_widget.Clock(
                update_interval=0.5,
                **theme.clock),

            qtile_widget.Wallpaper(
                wallpaper_command=None,
                directory=self.env.wallpaper_main_dir,
                **theme.wallpaper)
            if getattr(self.env, "wallpaper_main_dir", None)
            else None,

        ))), **theme.bar)

    def other_bar(self, theme):
        return bar.Bar(list(filter(lambda w: w is not None, (
            qtile_widget.GroupBox(
                visible_groups=["a", "s", "d", "f", "g"],
                **theme.groupbox),

            local_widget.TaskList(**theme.tasklist),

            local_widget.Clock(
                update_interval=0.5,
                **theme.clock),

            qtile_widget.Wallpaper(
                wallpaper_command=None,
                directory=self.env.wallpaper_other_dir,
                **theme.wallpaper)
            if getattr(self.env, "wallpaper_other_dir", None)
            else None,

        ))), **theme.bar)
