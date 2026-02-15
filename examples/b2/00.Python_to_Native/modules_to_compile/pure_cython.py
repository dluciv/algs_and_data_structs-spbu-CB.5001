#cython: language_level=3

class Fate:
    a: int = 524_287        # Mersenne prime
    b: int = 37
    c: int = 2_147_483_647  # Mersenne prive, found by Euler

    def __init__(self, seed: int = 1234567):
        self.r: int = seed

    def get_next(self)->int:
        self.r = (self.r * Fate.a + Fate.b) % Fate.c
        return self.r
