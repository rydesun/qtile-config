from libqtile.widget.tasklist import TaskList as _TaskList


class TaskList(_TaskList):
    def __init__(self, *args, **kwargs):
        self.defaults.extend((
            ("icon_offset_x", 0, ""),
            ("icon_offset_y", 0, ""),
        ))
        super().__init__(*args, **kwargs)

    def draw_icon(self, surface, offset):
        if not surface:
            return

        x = offset + self.borderwidth + self.padding_x + self.icon_offset_x
        y = self.padding_y + self.borderwidth + self.icon_offset_y

        self.drawer.ctx.save()
        self.drawer.ctx.translate(x, y)
        self.drawer.ctx.set_source(surface)
        self.drawer.ctx.paint()
        self.drawer.ctx.restore()

    def drawbox(self, offset, text, bordercolor, textcolor,
                width=None, rounded=False, block=False, icon=None):
        self.drawtext(text, textcolor, width)

        icon_padding = (self.icon_size + self.padding_x) if icon else 0
        padding_x = [self.padding_x + icon_padding, self.padding_x]

        framed = self.layout.framed(
            self.borderwidth,
            bordercolor,
            padding_x,
            [
                (self.bar.height - self.layout.height - self.borderwidth) / 2,
                (self.bar.height - self.layout.height + self.borderwidth) / 2
            ]
        )
        if block:
            framed.draw_fill(offset, self.margin_y, rounded)
        else:
            framed.draw_line(offset, self.margin_y, False)

        if icon:
            self.draw_icon(icon, offset)

    def button_press(self, x, y, button):
        if button == 2:
            window = self.get_clicked(x, y)
            if window:
                window.kill()
        else:
            return super().button_press(x, y, button)
