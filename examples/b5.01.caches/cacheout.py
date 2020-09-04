#!/usr/bin/env python3

import timeit

from cacheout import lru_memoize, lifo_memoize, fifo_memoize

@lifo_memoize(maxsize=10)
def fib_lifo(n):
    if n <= 2:
        return 1
    else:
        return fib_lifo(n-1) + fib_lifo(n-2)

@fifo_memoize(maxsize=10)
def fib_fifo(n):
    if n <= 2:
        return 1
    else:
        return fib_fifo(n-1) + fib_fifo(n-2)

@lru_memoize(maxsize=10)
def fib_lru(n):
    if n <= 2:
        return 1
    else:
        return fib_lru(n-1) + fib_lru(n-2)

n = 50

print(timeit.timeit(lambda: fib_lru(n), number=100))
print(timeit.timeit(lambda: fib_fifo(n), number=100))
print(timeit.timeit(lambda: fib_lifo(n), number=100))
