from datetime import datetime, timedelta, timezone

from libqtile.widget.base import InLoopPollText

from .base import Box
from .decoration import inject_decorations


@inject_decorations
class Clock(Box, InLoopPollText):
    DELTA = timedelta(seconds=0.5)

    defaults = [
        ("weekday_sign", tuple(range(1, 8)), ""),
        ("update_interval", 1.0, "Update interval for the clock"),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_defaults(self.defaults)

    def poll(self):
        now = datetime.now(timezone.utc).astimezone()
        return (now + self.DELTA).strftime(self.format).format(
            self.weekday_sign[now.weekday()])
