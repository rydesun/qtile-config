from libqtile.command import lazy
from libqtile.config import EzDrag, EzKey, Key


class Control:
    def __init__(self, env) -> None:
        self.env = env

    def keys(self, group_chars: str, scratchpad_names=None,
             scratchpad_chars=(str(i) for i in range(1, 10))):
        return [
            *(
                EzKey("M-"+char, lazy.group[char].toscreen())
                for char in group_chars
            ),
            *(
                EzKey("M-C-"+char, lazy.window.togroup(char))
                for char in group_chars
            ),

            *(
                EzKey('M-'+char,
                      lazy.group['scratchpad'].dropdown_toggle(name))
                for name, char in zip(scratchpad_names, scratchpad_chars)
            ),

            EzKey("M-<Return>", lazy.spawn(self.env.cmd_term)),
            EzKey("M-r", lazy.spawn(self.env.cmd_launcher)),

            EzKey("M-S-p", lazy.spawn(self.env.cmd_lock_screen)),
            EzKey("M-S-r", lazy.spawn(self.env.cmd_password_manager)),
            EzKey("M-S-f", lazy.spawn(self.env.cmd_screenshot)),
            EzKey("M-S-s", lazy.spawn(self.env.cmd_screenshot_select)),
            EzKey("M-S-w", lazy.spawn(self.env.cmd_screenshot_window)),
            EzKey("M-S-t", lazy.spawn(["bash", "-c", """text=$(zenity --entry)
                                       xdotool type --delay 150 $text"""])),

            EzKey("M-x", lazy.window.kill()),
            EzKey("M-q", lazy.window.toggle_minimize()),
            EzKey("M-w", lazy.window.toggle_floating()),

            EzKey("M-<Tab>", lazy.layout.toggle_split()),
            EzKey("M-j", lazy.layout.down()),
            EzKey("M-k", lazy.layout.up()),
            EzKey("M-h", lazy.layout.left()),
            EzKey("M-l", lazy.layout.right()),
            EzKey("M-n", lazy.group.next_window()),
            EzKey("M-p", lazy.group.prev_window()),

            EzKey("M-C-j", lazy.layout.shuffle_down()),
            EzKey("M-C-k", lazy.layout.shuffle_up()),
            EzKey("M-C-h", lazy.layout.shuffle_left()),
            EzKey("M-C-l", lazy.layout.shuffle_right()),

            EzKey("M-S-j", lazy.layout.grow_down()),
            EzKey("M-S-k", lazy.layout.grow_up()),
            EzKey("M-S-h", lazy.layout.grow_left()),
            EzKey("M-S-l", lazy.layout.grow_right()),
            EzKey("M-S-n", lazy.layout.normalize()),

            EzKey("M-C-r", lazy.reload_config()),
            EzKey("M-S-C-r", lazy.restart()),
            EzKey("M-S-C-q", lazy.shutdown()),

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
        ]

    def mouse(self):
        return [
            EzDrag("M-1", lazy.window.set_position_floating(),
                   start=lazy.window.get_position()),
            EzDrag("M-3", lazy.window.set_size_floating(),
                   start=lazy.window.get_size()),
        ]
