import random
import prime_number
import ext_euclidean

GALOIS_FIELDS = {}


class GF:
    p = 0

    def __init__(self, v):
        self.v = v % self.p

    def __str__(self):
        return f"{self.v}"

    def __repr__(self):
        return f"F{self.p}({self.v})"

    def __add__(s, o):
        v = s._get_other_value(o)
        return s.__class__((s.v + v) % s.p)

    def __sub__(s, o):
        v = s._get_other_value(o)
        return s.__class__((s.v - v) % s.p)

    def __mul__(s, o):
        v = s._get_other_value(o)
        return s.__class__((s.v * v) % s.p)

    def __floordiv__(s, o):
        v = s._get_other_value(o)
        return s.__class__((s.v * ext_euclidean.modinv(v, s.p)) % s.p)

    def __truediv__(s, o):
        return s.__floordiv__(o)

    def __eq__(s, o):
        v = s._get_other_value(o)
        return s.v == v

    @classmethod
    def _get_other_value(cls, other):
        if type(other) is cls:
            return other.v
        elif type(other) is int:
            return other
        else:
            raise Exception

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
        galois_field = type(
            f"GF{p}",
            (GF, ),
            {},
        )
        galois_field.p = p
        GALOIS_FIELDS[p] = galois_field
        return galois_field
