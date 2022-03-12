from libqtile.utils import lazify_imports
from libqtile.widget.import_error import make_error

widgets = {
    "Backlight": "backlight",
    "Box": "base",
    "Battery": "battery",
    "Clock": "clock",
    "Kdeconnect": "kdeconnect",
    "Net": "net",
    "TaskList": "tasklist",
    "ThermalSensor": "thermal_sensor",
    "Volume": "volume",
}

__all__, __dir__, __getattr__ = lazify_imports(
    widgets, __package__, fallback=make_error
)
