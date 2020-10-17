import time
from datetime import datetime, timezone

from libqtile.widget.clock import Clock as _Clock

from .base import TextBox


class Clock(TextBox, _Clock):
    clock_sign = ("🕛", "🕧", "🕐", "🕜", "🕑", "🕝",
                  "🕒", "🕞", "🕓", "🕟", "🕔", "🕠",
                  "🕕", "🕡", "🕖", "🕢", "🕗", "🕣",
                  "🕘", "🕤", "🕙", "🕥", "🕚", "🕦")
    weekday_sign = ("❶", "❷", "❸", "❹", "❺", "❻", "❼")

    def poll(self):
        if self.timezone:
            now = datetime.now(timezone.utc).astimezone(self.timezone)
        else:
            now = datetime.now(timezone.utc).astimezone()
        hour = now.hour
        if hour >= 12:
            hour -= 12
        if now.minute > 15 and now.minute <= 45:
            clock_index = hour * 2 + 1
        elif now.minute > 45:
            clock_index = hour * 2 + 2
        else:
            clock_index = hour * 2
        return (now + self.DELTA).strftime(self.format).format(
            self.clock_sign[clock_index], self.weekday_sign[now.weekday()])
