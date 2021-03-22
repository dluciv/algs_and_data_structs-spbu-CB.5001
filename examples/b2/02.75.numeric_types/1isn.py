#!/usr/bin/env python3

# https://github.com/python/cpython/blob/9a50ef43e42ee32450a81ce13ed5a0729d3b84e8/Objects/longobject.c#L23

from numba import njit

@njit(fastmath=True, nopython=True)
def check2(l0, l1):
    for e0, e1 in zip(l0, l1):
        if e0 is e1:
            print(e1)
        else:
            print(e1, hash(e0), hash(e1))

l0 = list(range(-50, 501, 50))
l1 = list(range(-50, 501, 50))
print("l0 <-> l1")
check2(l0, l1)

l2 = [int(float(e1)) for e1 in l1]
print("l1 <-> l2")
check2(l1, l2)

l3 = [e0 for e0 in l0] # l0.copy()
print("l0 <-> l3")
check2(l0, l3)
