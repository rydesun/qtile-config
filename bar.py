from libqtile import bar
from libqtile import widget as qtile_widget
from libqtile.command import lazy

import widget as local_widget


class Bar:
    def __init__(self, env):
        self.env = env

    def main_bar(self, theme):
        return bar.Bar([
            local_widget.Box(
                image_path=self.env.logo_file,
                text=self.env.logo_text,
                mouse_callbacks={
                    "Button1": lazy.spawn(self.env.cmd_menu),
                },
                **theme.menu_button),

            qtile_widget.GroupBox(
                visible_groups=["a", "s", "d", "f"],
                disable_drag=True,
                **theme.groupbox),

            qtile_widget.Spacer(length=10),

            local_widget.TaskList(**theme.tasklist),

            qtile_widget.Systray(**theme.systray),

            qtile_widget.Spacer(length=20),

            local_widget.Net(
                interface=self.env.dev_nic,
                **theme.netspeed),

            local_widget.Battery(
                low_percentage=0.2,
                update_interval=7,
                **theme.battery),

            local_widget.Kdeconnect(
                low_percentage=0.2,
                update_interval=7,
                dev_id=self.env.dev_kdeconnect,
                **theme.kdeconnect,
            ),

            local_widget.Backlight(
                backlight_name=self.env.dev_backlight,
                mouse_callbacks={
                    "Button4": lazy.spawn(self.env.cmd_backlight_increase),
                    "Button5": lazy.spawn(self.env.cmd_backlight_decrease),
                },
                **theme.backlight),

            local_widget.PulseVolume(
                **theme.volume),

            local_widget.ThermalSensor(
                dev_name=self.env.dev_thermal,
                **theme.thermalSensor),

            local_widget.Clock(
                update_interval=0.5,
                **theme.clock),

            qtile_widget.Wallpaper(
                random_selection=True,
                directory=self.env.wallpaper_dir,
                wallpaper_command=self.env.cmd_wallpaper,
                **theme.wallpaper),

        ], **theme.bar)

    def other_bar(self, theme):
        return bar.Bar([
            qtile_widget.GroupBox(
                visible_groups=["a", "s", "d", "f", "g"],
                **theme.groupbox),

            local_widget.TaskList(**theme.tasklist),

            local_widget.Clock(
                update_interval=0.5,
                **theme.clock),

            qtile_widget.Spacer(length=10),

        ], **theme.bar)
