#!/usr/bin/env python3

import timeit
import itertools
from fate0 import Fate as Fate0
from fate1 import Fate as Fate1
from fate2 import Fate as Fate2
from fate3 import Fate as Fate3

def load(fate_class):
    x = 0
    f = fate_class()
    for r in itertools.islice(f, 1_000_000):
        x = (x + r) % 2**60
    return x

print(load(Fate0), load(Fate1), load(Fate2), load(Fate3))

print(timeit.timeit(lambda: load(Fate0), number=10) / 10)
print(timeit.timeit(lambda: load(Fate1), number=10) / 10)
print(timeit.timeit(lambda: load(Fate2), number=10) / 10)
print(timeit.timeit(lambda: load(Fate3), number=10) / 10)
