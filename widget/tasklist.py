from libqtile.widget.tasklist import TaskList as _TaskList


class TaskList(_TaskList):
    defaults = [
        ("icon_offset_x", 0, ""),
        ("icon_offset_y", 0, ""),
        ("markup_floating_color", "#707070", ""),
        ("markup_maximized_color", "#707070", ""),
        ("markup_minimized_color", "#707070", ""),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_defaults(self.defaults)
        self.markup_floating = self.markup_floating.format(
            color=self.markup_floating_color)
        self.markup_maximized = self.markup_maximized.format(
            color=self.markup_minimized_color)
        self.markup_minimized = self.markup_minimized.format(
            color=self.markup_minimized_color)

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
        window = self.get_clicked(x, y)
        if not window:
            return super().button_press(x, y, button)
        if button == 2:
            window.kill()
        elif button == 3:
            for w in window.group.windows:
                if w == window or w.floating:
                    continue
                else:
                    w.minimized = True
            window.minimized = False

            if window.floating:
                window.bring_to_front()
        elif button == 4:
            window.move_up()
        elif button == 5:
            window.move_down()
        else:
            return super().button_press(x, y, button)
