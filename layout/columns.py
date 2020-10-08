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
            color = self.group.qtile.color_pixel(self.border_focus if col.split
                                                 else self.border_focus_stack)
        else:
            color = self.group.qtile.color_pixel(self.border_normal if col.split
                                                 else self.border_normal_stack)
        if len(self.columns) == 1 and (len(col) == 1 or not col.split):
            border = 0
        else:
            border = self.border_width
        width = int(
            0.5 + col.width * screen_rect.width * 0.01 / len(self.columns))
        x = screen_rect.x + int(0.5 + pos * screen_rect.width * 0.01 / len(self.columns))

        margin_left = 0 if n_col == 0 else self.margin
        margin_right = 0
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
            place_client(client,
                x,
                y,
                width - 2 * border,
                height - 2 * border,
                border,
                color,
                margin_left=margin_left,
                margin_right=margin_right,
                margin_top=margin_top,
                margin_bottom=margin_bottom,
            )
            client.unhide()
        elif client == col.cw:
            place_client(client,
                x,
                screen_rect.y,
                width - 2 * border,
                screen_rect.height - 2 * border,
                border,
                color,
                margin_left=margin_left,
                margin_right=margin_right,
                margin_top=margin_top,
                margin_bottom=margin_bottom,
            )
            client.unhide()
        else:
            client.hide()

def place_client(client, x, y, width, height, borderwidth, bordercolor,
                 above=False, margin_left=0, margin_right=0, margin_top=0, margin_bottom=0):
        send_notify = True

        x += margin_left
        y += margin_top
        width -= margin_left + margin_right
        height -= margin_top + margin_bottom

        # save x and y float offset
        if client.group is not None and client.group.screen is not None:
            client.float_x = x - client.group.screen.x
            client.float_y = y - client.group.screen.y

        client.x = x
        client.y = y
        client.width = width
        client.height = height
        client.borderwidth = borderwidth
        client.bordercolor = bordercolor

        kwarg = dict(
            x=x,
            y=y,
            width=width,
            height=height,
            borderwidth=borderwidth,
        )
        if above:
            kwarg['stackmode'] = StackMode.Above

        client.window.configure(**kwarg)

        if send_notify:
            client.send_configure_notify(x, y, width, height)

        if bordercolor is not None:
            client.window.set_attribute(borderpixel=bordercolor)
