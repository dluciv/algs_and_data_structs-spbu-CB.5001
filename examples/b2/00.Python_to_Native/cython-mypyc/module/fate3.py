# for mypyc

class Fate:
    def __init__(self, seed: int = 1234567):
        self.a: int = 524_287
        self.b: int = 37
        self.c: int = 2_147_483_647
        self.r: int = seed

    def __next__(self):
        self.r = (self.r * self.a + self.b) % self.c
        return self.r

    def __iter__(self):
        return self
