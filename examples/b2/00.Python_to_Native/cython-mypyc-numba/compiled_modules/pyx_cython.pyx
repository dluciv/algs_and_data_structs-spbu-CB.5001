cdef class Fate:
    cdef long long a, b, c, r  # int is not enough, it is 32 bit

    def __init__(self, int seed = 1234567):
        self.a = 524_287
        self.b = 37
        self.c = 2_147_483_647
        self.r = seed

    def get_next(self):
        self.r = (self.r * self.a + self.b) % self.c
        return self.r
