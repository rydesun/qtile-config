import time
from datetime import datetime, timezone

from libqtile.widget.clock import Clock as _Clock

from .base import TextBox


class Clock(TextBox, _Clock):
    weekday_sign = ("一", "二", "三", "四", "五", "六", "日")

    def poll(self):
        if self.timezone:
            now = datetime.now(timezone.utc).astimezone(self.timezone)
        else:
            now = datetime.now(timezone.utc).astimezone()
        return (now + self.DELTA).strftime(self.format).format(
            self.weekday_sign[now.weekday()])
