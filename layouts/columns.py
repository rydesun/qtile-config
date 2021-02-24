from libqtile.layout.columns import Columns as _Columns

class Columns(_Columns):
    def configure(self, client, screen_rect):
        pos = 0
        for n_col, col in enumerate(self.columns):
            if client in col:
                break
            pos += col.width
        else:
            client.hide()
            return

        if client.has_focus:
            color = self.border_focus if col.split else self.border_focus_stack
        else:
            color = self.border_normal if col.split else self.border_normal_stack

        if len(self.columns) == 1 and (len(col) == 1 or not col.split):
            border = 0
        else:
            border = self.border_width
        width = int(
            0.5 + col.width * screen_rect.width * 0.01 / len(self.columns))
        x = screen_rect.x + int(0.5 + pos * screen_rect.width * 0.01 / len(self.columns))

        margin_left = 0 if n_col == 0 else self.margin // 2
        margin_right = 0 if n_col == len(self.columns)-1 else self.margin // 2
        margin_top = self.margin
        margin_bottom = 0

        if col.split:
            pos = 0
            for n_line, c in enumerate(col):
                if client == c:
                    break
                pos += col.heights[c]
            height = int(
                0.5 + col.heights[client] * screen_rect.height * 0.01 / len(col))
            y = screen_rect.y + int(0.5 + pos * screen_rect.height * 0.01 / len(col))
            if n_line == 0:
                margin_top = 0
            client.place(
                x,
                y,
                width - 2 * border,
                height - 2 * border,
                border,
                color,
                margin=[margin_top, margin_right, margin_bottom, margin_left],
            )
            client.unhide()
        elif client == col.cw:
            margin_top = 1
            client.place(
                x,
                screen_rect.y,
                width - 2 * border,
                screen_rect.height - 2 * border,
                border,
                color,
                margin=[margin_top, margin_right, margin_bottom, margin_left],
            )
            client.unhide()
        else:
            client.hide()
