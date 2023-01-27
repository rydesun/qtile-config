import importlib


class ThemeLoader:
    def __init__(self, name="default", colorscheme="default") -> None:
        self._theme = importlib.import_module("theme."+name)
        self._colorscheme = importlib.import_module(
            "theme.colorscheme." + colorscheme)

    def __getattr__(self, __name: str):
        return getattr(self._theme, __name, {}) \
            | getattr(self._colorscheme, __name, {})
