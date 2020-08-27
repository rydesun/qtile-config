import time
from datetime import datetime, timezone

from libqtile.widget.clock import Clock as _Clock


class Clock(_Clock):
    weekday_sign = {
        "1": "❶",
        "2": "❷",
        "3": "❸",
        "4": "❹",
        "5": "❺",
        "6": "❻",
        "0": "❼",
    }

    def poll(self):
        if self.timezone:
            now = datetime.now(timezone.utc).astimezone(self.timezone)
        else:
            now = datetime.now(timezone.utc).astimezone()
        weekday = self.weekday_sign[now.strftime("%w")]
        return (now + self.DELTA).strftime(self.format) + weekday
