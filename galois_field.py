import random

import prime_number
import ext_euclidean

GALOIS_FIELDS = {}


class GF:
    p = 0

    def __init__(self, v):
        if type(v) is self.__class__:
            v = v.v
        self.v = v % self.p

    def __str__(self):
        return f"{self.v}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.v})"

    def __add__(s, o):
        v = s._get_other_value(o)
        return s.__class__((s.v + v) % s.p)

    __radd__ = __add__

    def __sub__(s, o):
        v = s._get_other_value(o)
        return s.__class__((s.v - v) % s.p)

    def __rsub__(s, o):
        v = s._get_other_value(o)
        return s.__class__((v - s.v) % s.p)

    def __neg__(s):
        return s.__class__(-s.v % s.p)

    def __mul__(s, o):
        v = s._get_other_value(o)
        return s.__class__((s.v * v) % s.p)

    def __floordiv__(s, o):
        v = s._get_other_value(o)
        return s.__class__((s.v * ext_euclidean.modinv(v, s.p)) % s.p)

    __truediv__ = __floordiv__

    def __eq__(s, o):
        v = s._get_other_value(o)
        return s.v == v

    @classmethod
    def _get_other_value(cls, other):
        other_type = type(other)
        if other_type is cls:
            return other.v
        elif other_type is type(cls.p):
            return other
        else:
            raise Exception

    def __hash__(self):
        return (self.__class__, self.p).__hash__()

    @classmethod
    def random(cls):
        return cls(random.randint(0, cls.p - 1))

    @classmethod
    def zero(cls):
        return cls(0)

    @classmethod
    def one(cls):
        return cls(1)


def GaloisField(p):
    if not prime_number.probably_prime(p):
        raise
    if p in GALOIS_FIELDS:
        return GALOIS_FIELDS[p]
    else:
        galois_field = type(f"GaloisField[{p}]", (GF,), {})
        galois_field.p = p
        GALOIS_FIELDS[p] = galois_field
        return galois_field


def is_galois_field(p):
    if type(p) is not type:
        p = type(p)
    return issubclass(p, GF)
