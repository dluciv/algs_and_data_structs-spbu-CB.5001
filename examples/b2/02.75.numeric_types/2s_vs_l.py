#!/usr/bin/env python3

from timeit import timeit
from numba import njit

def sum_n(about, how_many=1000000):
    res = about
    for _ in range(how_many):
        res += about
        res -= 1
        res -= about
        res *= 2
        res += 2
        res //= 2
    return res


def ttt(f):
    print(timeit(lambda: f(4),     number=10))
    print(timeit(lambda: f(300),   number=10))
    print(timeit(lambda: f(2**30), number=10))
    print(timeit(lambda: f(2**50), number=10))
    print(timeit(lambda: f(2**70), number=10))

j_sum_n = njit(nopython=True, fastmath=True)(sum_n)
j_sum_n(100)

print("----------")
ttt(sum_n)
print("----------")
ttt(j_sum_n)
