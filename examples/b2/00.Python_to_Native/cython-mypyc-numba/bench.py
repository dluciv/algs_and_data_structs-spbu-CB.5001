#!/usr/bin/env python3

import timeit

from pure_python import Fate as Fate0
from pure_cython import Fate as Fate1
from pyx_cython  import Fate as Fate2
from mypy_python import Fate as Fate3
from numba_jit   import Fate as Fate4

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
