from libqtile.widget.volume import Volume as _Volume


class Volume(_Volume):
    def _update_drawer(self):
        if self.volume <= 0:
            emoji = " "
        else:
            emoji = " "
        self.emoji = False
        super()._update_drawer()
        self.text = emoji + self.text
