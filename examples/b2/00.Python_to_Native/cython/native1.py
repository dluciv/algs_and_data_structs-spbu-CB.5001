#!/usr/bin/env python3

import timeit
import itertools
from ffate import Fate as Fate1
from ffate2 import Fate as Fate2

def load1():
    x = 0
    for r in itertools.islice(Fate1(), 1_000_000):
        x = (x + r) % 2**60
    return x

def load2():
    x = 0
    f = Fate2()
    for r in range(1_000_000):
        x = (x + f.get_next()) % 2**60
    return x

print(load1(), load2())

print(timeit.timeit(load1, number=10) / 10)
print(timeit.timeit(load2, number=10) / 10)
