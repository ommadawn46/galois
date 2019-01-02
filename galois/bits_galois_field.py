import random

import algebraic
import util
from encoding.reed_solomon.naive_rs import naive_a

POW_TABLE = [0] * 256
LOG_TABLE = [0] * 256
POLY_TABLE = [None] * 256

for d in range(255):
    poly = naive_a ** d
    bytes_data = util.pack_bin_list(poly.v)
    int_data = int.from_bytes(bytes_data, "big")
    POW_TABLE[d] = int_data
    LOG_TABLE[int_data] = d
    POLY_TABLE[int_data] = poly
LOG_TABLE[POW_TABLE[255]] = 255
POLY_TABLE[POW_TABLE[255]] = naive_a.zero()


# GF(2^8) for reed-solomon encording
class BitsGaloisField(algebraic.Set):
    def __init__(self, v):
        self.v = v

    def __str__(self):
        return f"{POLY_TABLE[self.v]}"

    def __repr__(self):
        return f"GF[2^8]({POLY_TABLE[self.v]})"

    def __add__(s, o):
        return s.__class__(s.v ^ o.v)

    __sub__ = __add__

    def __neg__(s):
        return s

    def __mul__(s, o):
        if s.v == 0 or o.v == 0:
            v = 0
        else:
            v = POW_TABLE[(LOG_TABLE[s.v] + LOG_TABLE[o.v]) % 255]
        return s.__class__(v)

    def __truediv__(s, o):
        if s.v == 0:
            v = 0
        elif o.v == 0:
            raise ZeroDivisionError("division by zero")
        else:
            v = POW_TABLE[(LOG_TABLE[s.v] - LOG_TABLE[o.v]) % 255]
        return s.__class__(v)

    __floordiv__ = __truediv__

    def __pow__(s, o):
        if not isinstance(o, int):
            raise
        if o == 0:
            return s.one()
        return s.__class__(POW_TABLE[(LOG_TABLE[s.v] * o) % 255])

    def __eq__(s, o):
        return s.v == o.v

    @classmethod
    def random(cls):
        return cls(random.randint(0, 255))

    @classmethod
    def zero(cls):
        return cls(0)

    @classmethod
    def one(cls):
        return cls(1)
