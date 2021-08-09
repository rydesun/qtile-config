import random

from . import ayu, onehalf, tokyo_night

__all__ = [
    'ayu',
    'tokyo_night',
    "onehalf"
]


def random_select():
    return random.choice([ayu, onehalf, tokyo_night])
