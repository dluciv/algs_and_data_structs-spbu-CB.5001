class Fate:
    a = 524_287       # Mersenne prime
    b = 37
    c = 2_147_483_647 # Mersenne prive, found by Euler

    def __init__(self, seed = 1234567):
        self.r = seed

    def __next__(self):
        self.r = (self.r * Fate.a + Fate.b) % Fate.c
        return self.r

    def __iter__(self):
        return self
