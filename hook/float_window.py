from functools import partial

from libqtile import hook


def register(rules):
    hook.subscribe.client_new(partial(match_floating, rules=rules))


def match_floating(c, rules):
    for rule in rules:
        if c.match(rule):
            c.match_floating = True
            return
    c.match_floating = False
