# for mypyc

class Fate:
    def __init__(self, seed: int = 1234567):
        self.a: int = 524_287
        self.b: int = 37
        self.c: int = 2_147_483_647
        self.r: int = seed

    def get_next(self):
        self.r: int = (self.r * self.a + self.b) % self.c
        return self.r
