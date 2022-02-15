cdef class Fate:
    cdef long a, b, c, r

    def __init__(self, int seed = 1234567):
        self.a = 524_287
        self.b = 37
        self.c = 2_147_483_647
        self.r = seed

    def __next__(self):
        self.r = (self.r * self.a + self.b) % self.c
        return self.r

    def __iter__(self):
        return self
