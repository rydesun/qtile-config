# https://github.com/qtile/qtile/discussions/2944

from libqtile import hook


def register():
    hook.subscribe.client_focus(set_hint)


def set_hint(window):
    window.window.set_property("IS_FLOATING", str(
        window.floating), type="STRING", format=8)
