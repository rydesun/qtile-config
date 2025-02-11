# https://github.com/qtile/qtile/discussions/2944

from libqtile import hook


def register():
    hook.subscribe.client_focus(set_hint)


def set_hint(window):
    window.window.set_property("IS_FLOATING", int(window.floating),
        type="CARDINAL", format=8)
