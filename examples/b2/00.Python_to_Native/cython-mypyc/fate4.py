from numba import int64
from numba.experimental import jitclass
from numba import jit

@jitclass([
  ('seed', int64),
  ('a', int64), ('b', int64), ('c', int64), ('r', int64)
])
class Fate:
    # class members are not supported yet by numba
    def __init__(self, seed: int = 1234567):
        self.a = 524_287        # Mersenne prime
        self.b = 37
        self.c = 2_147_483_647  # Mersenne prive, found by Euler
        self.r = seed

    def get_next(self):
        self.r = (self.r * self.a + self.b) % self.c
        return self.r
