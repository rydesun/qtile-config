import time
from datetime import datetime, timezone

from libqtile.widget import Clock as _Clock


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

    def _get_time(self):
        time.tzset()
        now = datetime.now(timezone.utc).astimezone()
        now += self.DELTA
        txt = now.strftime(self.format)
        weekday = self.weekday_sign[now.strftime("%w")]
        return txt + weekday
