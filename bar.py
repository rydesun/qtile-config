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
            and hasattr(self.env, "logo_text")
            else None,

            qtile_widget.GroupBox(
                visible_groups=["a", "s", "d", "f"],
                disable_drag=True,
                **theme.groupbox),

            local_widget.TaskList(**theme.tasklist),

            qtile_widget.Systray(**theme.systray)
            if qtile.core.name == "x11" else None,

            qtile_widget.Spacer(length=20),

            local_widget.Net(
                interface=self.env.dev_nic,
                mouse_callbacks={
                    "Button2": lazy.spawn(self.env.cmd_net_sniffer),
                },
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
                dev_headphone_sinks=self.env.dev_headphone_sinks,
                mouse_callbacks={
                    "Button2": lazy.spawn(self.env.cmd_volume_control),
                },
                **theme.volume),

            local_widget.ThermalSensor(
                dev_name=self.env.dev_thermal,
                **theme.thermalSensor)
            if getattr(self.env, "dev_thermal", None)
            else None,

            local_widget.Clock(
                update_interval=0.5,
                mouse_callbacks={
                    "Button2": lazy.spawn(self.env.cmd_calendar),
                },
                **theme.clock),

            local_widget.Wallpaper(
                default=self.env.wallpaper_main_default,
                dir=self.env.wallpaper_main_dir,
                **theme.wallpaper),

        ))), **theme.bar)

    def other_bar(self, theme):
        return bar.Bar(list(filter(lambda w: w is not None, (
            qtile_widget.GroupBox(
                visible_groups=["a", "s", "d", "f", "g"],
                **theme.groupbox),

            local_widget.TaskList(**theme.tasklist),

            local_widget.Clock(
                update_interval=0.5,
                mouse_callbacks={
                    "Button2": lazy.spawn(self.env.cmd_calendar),
                },
                **theme.clock),

            local_widget.Wallpaper(
                default=self.env.wallpaper_other_default,
                dir=self.env.wallpaper_other_dir,
                **theme.wallpaper),

        ))), **theme.bar)
