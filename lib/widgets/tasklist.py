from libqtile.widget import TaskList as _TaskList


class TaskList(_TaskList):
    _TaskList.defaults.extend((
        ("icon_offset_x", 0),
        ("icon_offset_y", 0),
    ))
    def draw_icon(self, surface, offset):
        if not surface:
            return

        x = offset + self.borderwidth + self.padding_x + 2 + self.icon_offset_x
        y = self.padding_y + self.borderwidth + self.icon_offset_y

        self.drawer.ctx.save()
        self.drawer.ctx.translate(x, y)
        self.drawer.ctx.set_source(surface)
        self.drawer.ctx.paint()
        self.drawer.ctx.restore()
