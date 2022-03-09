from .types import Colors


class Theme:
    def __init__(self, colors: Colors):
        self.init_layouts(colors)
        self.init_widgets(colors)

    def init_layouts(self, colors: Colors) -> None:
        self.layout_floating = dict(
            border_width=0,
            border_focus=colors.color0,
            border_normal=colors.color0,
        )
        self.layout_column = dict(
            border_width=0,
        )
        self.dropdown_window = dict(
            x=0.2,
            y=0.1,
            width=0.6,
            height=0.7,
        )

    def init_widgets(self, colors: Colors) -> None:
        font_sans = "sans"
        font_mono = "monospace"
        fontsize = 16
        fontsize_with_decoration = 14

        self.bar = dict(
            size=34,
            opacity=0.95,

            background=colors.color_background,
        )

        self.widget_defaults = dict(
            font=font_sans,
            fontsize=fontsize,

            foreground=colors.color_foreground,
            fontshadow=colors.color_shadow,
        )

        self.menu_button = dict(
            margin_x=3,
            margin_y=3,
            fontshadow=None,
        )

        self.groupbox = dict(
            font=font_mono,
            fontsize=fontsize,
            borderwidth=2,
            margin_x=8,
            spacing=3,
            highlight_method="line",

            background=colors.color8,
            highlight_color=colors.color8,
            inactive=colors.color0,
            active=colors.color_major,
            this_current_screen_border=colors.color_major,
            this_screen_border=colors.color_major,
            other_current_screen_border=colors.color_minor,
            other_screen_border=colors.color_minor,
            urgent_border=colors.color_urgent,
        )

        self.tasklist = dict(
            title_width_method="uniform",
            max_title_width=200,
            spacing=12,
            fontsize=fontsize_with_decoration,
            icon_size=20,
            margin_y=0,
            padding_x=5,
            padding_y=4,
            icon_offset_x=0,
            icon_offset_y=1.3,
            markup_floating="  <span foreground='%s'></span>   {}"
            % colors.color14,
            markup_maximized="  <span foreground='%s'></span>   {}"
            % colors.color14,
            markup_minimized="  <span foreground='%s'></span>   {}"
            % colors.color14,
            borderwidth=2,

            border=colors.color_major,
            unfocused_border=colors.color_common,
            urgent_border=colors.color_urgent,
        )

        self.systray = dict(
            icon_size=22,
        )

        self.kdeconnect = dict(
            format="{extra_icon}{icon}{percent: .0f}",
            icon_charge=" ",
            icon_discharge="",
            icon_full_energy="",
            icon_high_energy="",
            icon_half_energy="",
            icon_low_energy="",
            icon_empty_energy="",
            extra_offsetx=3,
            extra_offsety=-1.5,

            foreground=colors.color4,
            foreground_discharge=colors.color3,
            foreground_low=colors.color5,
        )

        self.netspeed = dict(
            icon_upload="",
            icon_download="",
            font=font_mono,
            extra_offsety=0.3,

            foreground=colors.color15,
        )

        self.battery = dict(
            format="{extra_icon} {icon}{percent: .0f}",
            icon_charge="",
            icon_discharge="",
            icon_plug="",
            icon_full_energy="",
            icon_high_energy="",
            icon_half_energy="",
            icon_low_energy="",
            icon_empty_energy="",
            foreground_discharge=colors.color3,
            foreground_low=colors.color5,
            extra_offsetx=5,
            extra_offsety=-0.7,

            foreground=colors.color_healthy,
        )

        self.volume = dict(
            icon=" ",
            icon_mute="婢 ",
            extra_offsety=-1.5,

            foreground=colors.color15,
        )

        self.thermalSensor = dict(
            icon=" ",
            extra_offsety=-1.4,

            foreground=colors.color_healthy,
            foreground_alert=colors.color5,
        )

        self.backlight = dict(
            format="{percent: .0f}",
            extra_offsety=-1.5,

            foreground=colors.color15,
        )

        self.clock = dict(
            format="%H:%M:%S  %m-%d  <span rise='1000' size='small'>{}</span>",
            weekday_sign=(
                "周一",
                "周二",
                "周三",
                "周四",
                "周五",
                "周六",
                "周日",
            ),
            extra_offsety=-1,

            foreground=colors.color15,
        )

        self.wallpaper = dict(
            label=" ",
            extra_offsety=-1,

            foreground=colors.color15,
        )
