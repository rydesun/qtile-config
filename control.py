from libqtile.command import lazy
from libqtile.config import EzDrag, EzKey, Key, KeyChord
from libqtile.scratchpad import ScratchPad


class Control:
    def __init__(self, env) -> None:
        self.env = env

    def keys(self):
        return [
            # {{{ 操作单个窗口
            KeyChord(["mod4"], "w", name="Window", submappings=[
                EzKey("M-f", lazy.window.toggle_floating()),
                EzKey("M-c", lazy.window.center()),
                EzKey("M-v", lazy.window.toggle_minimize()),
                EzKey("M-q", lazy.window.toggle_fullscreen()),
                EzKey("M-x", lazy.window.kill()),
                EzKey("M-t", lazy.window.bring_to_front()),
            ]),
            KeyChord(["mod4"], "m", name="MoveWindow", mode=True, submappings=[
                EzKey("M-f", lazy.window.toggle_floating()),
                EzKey("M-c", lazy.window.center()),
                EzKey("M-h", lazy.window.move_floating(-20, 0)),
                EzKey("M-l", lazy.window.move_floating(20, 0)),
                EzKey("M-j", lazy.window.move_floating(0, 20)),
                EzKey("M-k", lazy.window.move_floating(0, -20)),
                EzKey("M-y", lazy.window.move_floating(-20, -20)),
                EzKey("M-u", lazy.window.move_floating(20, -20)),
                EzKey("M-b", lazy.window.move_floating(-20, 20)),
                EzKey("M-n", lazy.window.move_floating(20, 20)),
                EzKey("M-S-h", lazy.window.resize_floating(-20, 0)),
                EzKey("M-S-l", lazy.window.resize_floating(20, 0)),
                EzKey("M-S-j", lazy.window.resize_floating(0, 20)),
                EzKey("M-S-k", lazy.window.resize_floating(0, -20)),
                EzKey("M-S-y", lazy.window.resize_floating(-20, -20)),
                EzKey("M-S-u", lazy.window.resize_floating(20, -20)),
                EzKey("M-S-b", lazy.window.resize_floating(-20, 20)),
                EzKey("M-S-n", lazy.window.resize_floating(20, 20)),
            ]),
            # }}}

            # {{{ 移动窗口焦点 (保持布局)
            EzKey("M-n", lazy.group.next_window()),
            EzKey("M-p", lazy.group.prev_window()),
            EzKey("M-j", lazy.layout.down()),
            EzKey("M-k", lazy.layout.up()),
            EzKey("M-h", lazy.layout.left()),
            EzKey("M-l", lazy.layout.right()),
            # }}}

            # {{{ 操作Group
            # 显示指定的Group
            *(Key(["mod4"], i["key"], lazy.group[i["key"]].toscreen())
              for i in self.env.groups),

            # 移动窗口到指定的Group
            *(Key(["mod4", "control"], i["key"], lazy.window.togroup(i["key"]))
              for i in self.env.groups),
            # }}}

            # {{{ 调整布局 (尺寸稳定)
            EzKey("M-C-j", lazy.layout.shuffle_down()),
            EzKey("M-C-k", lazy.layout.shuffle_up()),
            EzKey("M-C-h", lazy.layout.shuffle_left()),
            EzKey("M-C-l", lazy.layout.shuffle_right()),
            # }}}

            # {{{ 调整布局 (改变尺寸)
            EzKey("M-S-s", lazy.layout.toggle_split()),
            EzKey("M-S-n", lazy.layout.normalize()),
            EzKey("M-S-j", lazy.layout.grow_down()),
            EzKey("M-S-k", lazy.layout.grow_up()),
            EzKey("M-S-h", lazy.layout.grow_left()),
            EzKey("M-S-l", lazy.layout.grow_right()),
            # }}}

            # {{{ 启动外部程序
            EzKey("M-<Return>", lazy.spawn(self.env.cmd_term)),
            EzKey("M-r", lazy.spawn(self.env.cmd_launcher)),
            EzKey("M-o", bind_window(self.env.groups)),

            KeyChord(["mod4"], "e", name="Execute", submappings=[
                Key(["mod4"], i["key"], lazy.spawn(i['cmd']))
                for i in self.env.cmd_bindings
            ]),

            KeyChord(["mod4"], "c", name="Capture", submappings=[
                EzKey("M-f", lazy.spawn(self.env.cmd_screenshot_fullscreen)),
                EzKey("M-s", lazy.spawn(self.env.cmd_screenshot_select)),
                EzKey("M-w", lazy.spawn(self.env.cmd_screenshot_window)),
            ]),

            KeyChord(["mod4"], "t", name="ScratchPad", submappings=[
                Key(["mod4"], i["key"], lazy.group['default_scratchpad'].
                    dropdown_toggle(i["name"]))
                for i in self.env.dropdowns
            ]),
            # }}}

            # {{{ Qtile
            KeyChord(["mod4"], "q", [
                EzKey("M-r", lazy.reload_config()),
                EzKey("M-C-r", lazy.reload_config()),
                EzKey("M-C-q", lazy.shutdown()),
            ], name="Qtile"),
            # }}}

            # {{{ XF86
            Key([], "XF86AudioMute", lazy.spawn(
                self.env.cmd_volume_toggle)),
            Key([], "XF86AudioLowerVolume", lazy.spawn(
                self.env.cmd_volume_decrease)),
            Key([], "XF86AudioRaiseVolume", lazy.spawn(
                self.env.cmd_volume_increase)),
            Key([], "XF86MonBrightnessUp", lazy.spawn(
                self.env.cmd_backlight_increase)),
            Key([], "XF86MonBrightnessDown", lazy.spawn(
                self.env.cmd_backlight_decrease)),
            # }}}
        ]

    def mouse(self):
        return [
            EzDrag("M-1", lazy.window.set_position_floating(),
                   start=lazy.window.get_position()),
            EzDrag("M-3", lazy.window.set_size_floating(),
                   start=lazy.window.get_size()),
        ]


@lazy.function
def bind_window(qtile, groups):
    for g in groups:
        if g["key"] != qtile.current_group.name:
            continue
        rule = g["bind_window"]
        for w in qtile.windows_map.values():
            if w.group \
                    and not isinstance(w.group, ScratchPad) \
                    and w.match(rule["match"]):
                w.togroup(qtile.current_group.name)
                return
        qtile.cmd_spawn(rule["cmd"])
        return

# vim:fdm=marker
