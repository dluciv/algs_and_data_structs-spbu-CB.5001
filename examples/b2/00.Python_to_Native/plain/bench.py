#!/usr/bin/env python3

import timeit
import itertools
from fate import Fate

def load():
    x = 0
    for r in itertools.islice(Fate(), 1_000_000):
        x = (x + r) % 2**60
    return x

print(load())

print(timeit.timeit(load, number=5) / 5)
