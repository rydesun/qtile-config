import random

from . import ayu, ayu_mirage, onehalf, tokyo_night

__all__ = [
    'ayu',
    'ayu_mirage',
    'tokyo_night',
    "onehalf"
]


def random_select():
    return random.choice([ayu, ayu_mirage, onehalf, tokyo_night])
