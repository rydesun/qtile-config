from libqtile.command import lazy

@lazy.function
def disable_all_floating(qtile):
    for window in qtile.current_group.windows:
        window.floating = False

@lazy.function
def bring_all_floating_to_front(qtile):
    for window in qtile.current_group.windows:
        if window.floating:
            window.cmd_bring_to_front()
