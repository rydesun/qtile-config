from libqtile.log_utils import logger
from libqtile.utils import send_notification


class EnvLoader:
    def __init__(self) -> None:
        try:
            import env
        except ImportError:
            logger.warning("env.py is missing")
            send_notification("Configuration warning",
                              "env.py is missing. Use env_example.py instead.")
            import env_example as env
        self._env = env

        self.total_screens = getattr(env, "total_screens", 1)
        self.float_rules = getattr(env, "float_rules", [])
        self.float_config = getattr(env, "float_config", [])
        self.dropdowns = getattr(env, "dropdowns", [])
        self.groups = getattr(env, "groups", [
            {"key": "0", "bind_window": {}},
        ])

    def __getattr__(self, __name: str):
        if hasattr(self._env, __name):
            return getattr(self._env, __name)

        match __name:
            case 'cmd_term':
                from libqtile.utils import guess_terminal
                cmd_term = [guess_terminal()]
                return cmd_term
            case s if s.startswith("cmd_"):
                return ["false"]
            case s if s.startswith("wallpaper_"):
                return ""
            case _:
                raise AttributeError
