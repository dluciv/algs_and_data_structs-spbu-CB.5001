#cython: language_level=3

class Fate:
    a = 524_287        # Mersenne prime
    b = 37
    c = 2_147_483_647  # Mersenne prive, found by Euler

    def __init__(self, seed: int = 1234567):
        self.r = seed

    def get_next(self):
        self.r = (self.r * Fate.a + Fate.b) % Fate.c
        return self.r
