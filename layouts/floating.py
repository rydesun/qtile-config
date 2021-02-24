from typing import Dict, List, Optional

from libqtile.layout.floating import Floating as _Floating


class Floating(_Floating):
    def __init__(self, border_rules: Optional[List[Dict]] = None, *args, **kwargs):
        self.border_rules = border_rules
        super().__init__(*args, **kwargs)
        self.init_border_width = self.border_width

    def configure(self, client, screen_rect):
        border_width = self.init_border_width
        if self.border_rules:
            for rule in self.border_rules:
                if rule["match"].compare(client):
                    border_width = rule["border_width"]
                    break
        self.border_width = border_width
        super().configure(client, screen_rect)
