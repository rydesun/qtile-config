class Color:
    foreground = "#0ed2d5"
    foreground_soft = "#56b6c2"
    foreground_hard = "#dcdfe4"
    background = "#282c34"
    shadow = "#000000"

    sudden = "#e06c75"
    danger = "#c678dd"
    notice = "#e5c07b"
    hint = "#61afef"
    safe = "#58d379"
    major = "#58d379"
    minor = background

    idx1 = "#1d677a"

    def __init__(self):
        self.init_layout()
        self.init_bar()
        self.init_widget()

    def init_layout(self):
        self.layout_floating = dict(
            border_focus=self.background,
            border_normal=self.background,
        )

    def init_bar(self):
        self.bar = dict(
            opacity=1,
            background=self.background,
        )

    def init_widget(self):
        self.widget_defaults = dict(
            foreground=self.foreground_soft,
            fontshadow=self.shadow,
        )
        self.menu_button = dict(
            fontshadow=None,
        )
        self.groupbox = dict(
            background=self.idx1,
            highlight_color=self.idx1,
            inactive=self.background,
            active=self.major,
            this_current_screen_border=self.major,
            this_screen_border=self.major,
            other_current_screen_border=self.minor,
            other_screen_border=self.minor,
            urgent_border=self.sudden,
        )
        self.tasklist = dict(
            _icon_floating=self.foreground_soft,
            _icon_maximized=self.foreground_soft,
            _icon_minimized=self.foreground_soft,
            foreground=self.foreground_hard,
            border=self.major,
            unfocused_border=self.hint,
            urgent_border=self.sudden,
        )
        self.netspeed = dict(
            foreground=self.foreground,
        )
        self.battery = dict(
            foreground=self.safe,
            foreground_discharge=self.notice,
            foreground_low=self.danger,
        )
        self.kdeconnect = dict(
            foreground=self.hint,
            foreground_discharge=self.notice,
            foreground_low=self.danger,
        )
        self.backlight = dict(
            foreground=self.foreground,
        )
        self.volume = dict(
            foreground=self.foreground,
        )
        self.thermalSensor = dict(
            foreground=self.safe,
            foreground_alert=self.danger,
        )
        self.clock = dict(
            foreground=self.foreground,
        )
        self.wallpaper = dict(
            foreground=self.foreground,
        )
