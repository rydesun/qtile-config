import importlib


class ThemeLoader:
    def __init__(
        self,
        default_file="default",
        default_colors_file="default",
        override_file = "override",
    ) -> None:
        self._theme = importlib.import_module("theme."+default_file)
        self._colors = importlib.import_module(
            "theme.colors." + default_colors_file)
        try:
            self.override = importlib.import_module("theme."+override_file)
        except ModuleNotFoundError:
            self.override = {}

    def __getattr__(self, __name: str):
        return getattr(self._theme, __name, {}) \
            | getattr(self._colors, __name, {}) \
            | getattr(self.override, __name, {})
