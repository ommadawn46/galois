import random

import algebraic
import util

GALOIS_FIELDS = {}


class GF(algebraic.Set):
    def __init__(self, v):
        if isinstance(v, self.__class__):
            v = v.v
        if not isinstance(v, type(self.p)):
            v = type(self.p)(v)
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
        return s.__class__((s.v * util.modinv(v, s.p)) % s.p)

    __truediv__ = __floordiv__

    def __eq__(s, o):
        v = s._get_other_value(o)
        return s.v == v

    @classmethod
    def _get_other_value(cls, other):
        if isinstance(other, cls):
            return other.v
        elif isinstance(other, type(cls.p)):
            return other
        else:
            raise Exception

    def __hash__(self):
        return (self.__class__, self.p, self.v).__hash__()

    @classmethod
    def random(cls):
        if isinstance(cls.p, algebraic.Set):
            return cls(cls.p.random())
        if isinstance(cls.p, int):
            return cls(random.randint(0, cls.p - 1))
        raise

    @classmethod
    def zero(cls):
        return cls(cls.p_zero)

    @classmethod
    def one(cls):
        return cls(cls.p_one)


def GaloisField(p):
    if p in GALOIS_FIELDS:
        return GALOIS_FIELDS[p]
    else:
        galois_field = type(f"GaloisField[{p}]", (GF,), {})
        galois_field.p = p
        galois_field.p_zero = p.zero() if isinstance(p, algebraic.Set) else 0
        galois_field.p_one = p.one() if isinstance(p, algebraic.Set) else 1
        GALOIS_FIELDS[p] = galois_field
        return galois_field
