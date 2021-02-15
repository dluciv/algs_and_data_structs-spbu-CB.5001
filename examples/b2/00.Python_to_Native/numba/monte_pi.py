#!/usr/bin/env python3

from numba import jit, prange
import random
import timeit

@jit(nopython=True, parallel=True)
def monte_carlo_pi(nsamples = 1_000_000):
    acc = 0
    for i in prange(4):
        tacc = 0
        for j in range(nsamples // 4):
            x = random.random()
            y = random.random()
            if (x ** 2 + y ** 2) < 1.0:
                tacc += 1
        acc += tacc
    return 4.0 * acc / nsamples

print(timeit.timeit(monte_carlo_pi, number=1))

print(monte_carlo_pi())

print(timeit.timeit(monte_carlo_pi, number=30) / 30)
