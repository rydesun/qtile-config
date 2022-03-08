from datetime import datetime, timedelta, timezone

from libqtile.widget.base import InLoopPollText

from .base import TextBox


class Clock(TextBox, InLoopPollText):
    DELTA = timedelta(seconds=0.5)

    def __init__(self, *args, **kwargs):
        self.defaults.extend((
            ("weekday_sign", tuple(range(1, 8)), ""),
            ("update_interval", 1.0, "Update interval for the clock"),

        ))
        super().__init__(*args, **kwargs)

    def poll(self):
        now = datetime.now(timezone.utc).astimezone()
        return (now + self.DELTA).strftime(self.format).format(
            self.weekday_sign[now.weekday()])
