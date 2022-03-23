class Theme:
    def __init__(self, color, scale_factor=1):
        self.color = color
        self.scale_factor = scale_factor
        self.init_layout()
        self.init_window()
        self.init_bar()
        self.init_widget()

    def scale(self, val, rounded=False):
        scaled = self.scale_factor * val
        return round(scaled) if rounded else scaled

    def init_layout(self):
        self.layout_column = dict(
            border_width=self.scale(0),
        )
        self.layout_floating = dict(
            border_width=self.scale(0),
            **self.color.layout_floating,
        )

    def init_window(self):
        self.dropdown_window = dict(
            x=0.2,
            y=0.1,
            width=0.6,
            height=0.7,
        )

    def init_bar(self):
        self.bar = dict(
            size=self.scale(32, rounded=True),
            **self.color.bar,
        )

    def init_widget(self):
        self.widget_defaults = dict(
            font="sans",
            fontsize=self.scale(16, rounded=True),
            **self.color.widget_defaults,
        )
        self.menu_button = dict(
            margin_x=self.scale(3),
            margin_y=self.scale(3),
            extra_offsety=self.scale(-1),
            **self.color.menu_button,
        )
        self.groupbox = dict(
            font="monospace",
            margin_x=self.scale(8),
            spacing=self.scale(3),
            borderwidth=self.scale(2),
            highlight_method="line",
            **self.color.groupbox,
        )
        self.tasklist = dict(
            fontsize=self.scale(14, rounded=True),
            icon_size=self.scale(20),
            title_width_method="uniform",
            max_title_width=self.scale(200),
            spacing=self.scale(12),
            margin_y=self.scale(0),
            padding_x=self.scale(8),
            icon_offset_x=self.scale(0),
            icon_offset_y=self.scale(0),
            borderwidth=self.scale(2),
            markup_floating="  <span foreground='%s'></span>   {}"
            % self.color.tasklist["_icon_floating"],
            markup_maximized="  <span foreground='%s'></span>   {}"
            % self.color.tasklist["_icon_maximized"],
            markup_minimized="  <span foreground='%s'></span>   {}"
            % self.color.tasklist["_icon_minimized"],
            **self.color.tasklist,
        )
        self.systray = dict(
            icon_size=self.scale(22, rounded=True),
        )
        self.netspeed = dict(
            font="monospace",
            icon_upload="",
            icon_download="",
            extra_offsety=self.scale(0.3),
            **self.color.netspeed
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
            extra_offsetx=self.scale(5),
            extra_offsety=self.scale(-0.7),
            **self.color.battery,
        )
        self.kdeconnect = dict(
            format="{extra_icon}{icon}{percent: .0f}",
            icon_charge=" ",
            icon_discharge="",
            icon_plug="",
            icon_full_energy="",
            icon_high_energy="",
            icon_half_energy="",
            icon_low_energy="",
            icon_empty_energy="",
            extra_offsetx=self.scale(3),
            extra_offsety=self.scale(-1.5),
            **self.color.kdeconnect
        )
        self.backlight = dict(
            format="{percent: .0f}",
            extra_offsety=self.scale(-1.5),
            **self.color.backlight,
        )
        self.volume = dict(
            icon=" ",
            icon_mute="婢 ",
            icon_headphone=" ",
            icon_headphone_mute=" ",
            mute_text="M",
            extra_offsety=self.scale(-1.5),
            **self.color.volume,
        )
        self.thermalSensor = dict(
            icon=" ",
            extra_offsety=self.scale(-1.4),
            **self.color.thermalSensor,
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
            extra_offsety=self.scale(-1),
            **self.color.clock,
        )
        self.wallpaper = dict(
            fmt="tile",
            font="mono",
            extra_offsety=self.scale(-1),
        )
