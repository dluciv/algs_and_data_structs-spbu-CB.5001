#!/usr/bin/env python3

import timeit
import itertools
from fate0 import Fate as Fate0
from fate1 import Fate as Fate1
from fate2 import Fate as Fate2
from fate3 import Fate as Fate3
from fate4 import Fate as Fate4

def load(fate_class):
    f = fate_class()
    for _ in range(1_000_000):
        r = f.get_next()
    return r

def test(fate_class):
    f = fate_class()
    for _ in range(1_000):
        r = f.get_next()
    return r

for fc in [Fate0, Fate1, Fate2, Fate3, Fate4]:
    print(fc, test(fc), timeit.timeit(lambda: load(fc), number=10) / 10)
