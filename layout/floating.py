from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from libqtile.config import Match
    from typing import Dict, List, Optional

from libqtile.layout.floating import Floating as _Floating


class Floating(_Floating):
    def __init__(self,
                 float_config: Optional[List[Dict]] = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_config = float_config
        self.prime_border_width = self.border_width

    def configure(self, client, screen_rect):
        border_width = self.prime_border_width
        if self.client_config:
            for rule in self.client_config:
                if rule["match"].compare(client):
                    border_width = rule["border_width"]
                    break
        self.border_width = border_width
        super().configure(client, screen_rect)

    def match(self, win):
        return win.match_floating
