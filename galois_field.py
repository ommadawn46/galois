import random
import prime_number
import ext_euclidean

class Fp:
    p = 0

    def __init__(self, v):
        self.v = v % self.p

    def __str__(self):
        return f"{self.v}"

    def __repr__(self):
        return f"F{self.p}({self.v})"

    @classmethod
    def _get_other_value(cls, other):
        if type(other) is cls:
            return other.v
        elif type(other) is int:
            return other
        else:
            raise Exception

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

GaloisFields = {}
def GaloisField(p):
    if not prime_number.probably_prime(p):
        raise
    if p in GaloisFields:
        return GaloisFields[p]
    else:
        galois_field = type(
            f"F{p}",
            (Fp, ),
            {},
        )
        galois_field.p = p
        GaloisFields[p] = galois_field
        return galois_field

if __name__ == '__main__':
    p = 3
    while p <= 10000:
        p = prime_number.next_prime(p)

        GF = GaloisField(p)
        zero, one = GF(0), GF(1)

        a = GF(random.randint(2, p-1))
        b = GF(random.randint(2, p-1))
        c = GF(random.randint(2, p-1))
        while a == b or b == c or c == a:
            a = GF(random.randint(2, p-1))
            b = GF(random.randint(2, p-1))
            c = GF(random.randint(2, p-1))

        # Group
        assert(a + (b+c) == (a+b) + c)
        assert(a + zero == a)
        assert(a - a == zero)

        # Abelian Group
        assert(a + b == b + a)

        # Ring
        assert(a * (b*c) == (a*b) * c)
        assert(a * (b+c) == a*b + a*c)
        assert((a+b) * c == a*c + b*c)

        # Commutative Ring
        assert(a * b == b * a)

        # Integral Domain
        assert(a * one == a)
        assert(a * zero == zero)

        # Field
        assert(a * (one / a) == one)
