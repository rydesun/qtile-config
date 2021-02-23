from datetime import datetime, timezone

from libqtile.widget.clock import Clock as _Clock

from .base import TextBox


class Clock(TextBox, _Clock):
    def __init__(self, *args, **kwargs):
        self.defaults.extend((
            ("weekday_sign", tuple(range(1,8)), ""),
        ))
        super().__init__(*args, **kwargs)

    def poll(self):
        if self.timezone:
            now = datetime.now(timezone.utc).astimezone(self.timezone)
        else:
            now = datetime.now(timezone.utc).astimezone()
        return (now + self.DELTA).strftime(self.format).format(
            self.weekday_sign[now.weekday()])
