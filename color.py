class Color:
    foreground = "#0ec2c5"
    foreground_soft = "#56b6c2"
    foreground_hard = "#dcdfe4"
    background = "#14272d"
    background_blob = "#215578"
    shadow = "#000000"

    sudden = "#e06c75"
    danger = "#b678ad"
    notice = "#a5a07b"
    hint = "#33a3a8"
    safe = "#58b379"
    major = safe
    minor = "#1d677a"

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
            foreground=self.foreground,
            fontshadow=self.shadow,
        )
        self.menu_button = dict(
            fontshadow=None,
        )
        self.groupbox = dict(
            background=self.minor,
            highlight_color=self.minor,
            inactive=self.background,
            active=self.major,
            this_current_screen_border=self.major,
            this_screen_border=self.major,
            other_current_screen_border=self.background,
            other_screen_border=self.background,
            urgent_border=self.sudden,
        )
        self.tasklist = dict(
            _icon_floating=self.foreground_soft,
            _icon_maximized=self.foreground_soft,
            _icon_minimized=self.foreground_soft,
            foreground=self.foreground_hard,
            border=self.major,
            unfocused_border=self.minor,
            urgent_border=self.sudden,
        )
        self.netspeed = dict()
        self.battery = dict(
            foreground=self.safe,
            foreground_discharge=self.notice,
            foreground_low=self.danger,
        )
        self.kdeconnect = dict(
            foreground=self.hint,
            foreground_discharge=self.hint,
            foreground_low=self.danger,
        )
        self.backlight = dict()
        self.volume = dict()
        self.thermalSensor = dict(
            foreground=self.safe,
            foreground_alert=self.danger,
        )
        self.clock = dict()
        self.wallpaper = dict(
            foreground=self.foreground_hard,
            _decoration=self.background_blob,
            fontshadow=None,
        )
