import random
from enum import IntEnum, auto

import prime_number
import galois_field
import bool_polynomial_ring


class AlgebraicStructure(IntEnum):
    SET = auto()
    GROUP = auto()
    ABELIAN_GROUP = auto()
    RING = auto()
    COMMUTATIVE_RING = auto()
    INTEGRAL_DOMAIN = auto()
    FIELD = auto()

    @classmethod
    def check(cls, A):
        zero, one = A.zero(), A.one()

        a = b = c = None
        while a == b    or b == c    or c == a    or \
              a == zero or b == zero or c == zero or \
              a == one  or b == one  or c == one:
            a = A.random()
            b = A.random()
            c = A.random()

        is_group = False
        try:
            is_group = all([
                a + (b+c) == (a+b) + c,
                a + zero == a,
                a - a == zero
            ])
        except:
            pass
        if not is_group:
            return cls.SET

        if not a + b == b + a:
            return cls.GROUP

        is_ring = False
        try:
            is_ring = all([
                a * (b*c) == (a*b) * c,
                a * (b+c) == a*b + a*c,
                (a+b) * c == a*c + b*c
            ])
        except:
            pass
        if not is_ring:
            return cls.ABELIAN_GROUP

        if not a * b == b * a:
            return cls.RING

        if not (
            a * one == a and
            a * zero == zero ):
            return cls.COMMUTATIVE_RING

        is_field = False
        try:
            is_field = a * (one / a) == one
        except:
            pass
        if not is_field:
            return cls.INTEGRAL_DOMAIN

        return cls.FIELD


def galois_field_test():
    p = prime_number.next_prime(10000)
    GF = galois_field.GaloisField(p)
    struct = AlgebraicStructure.check(GF)
    print(GF.__name__, 'is', struct)


def bool_polynomial_ring_test():
    BPR = bool_polynomial_ring.BooleanPolynomialRing
    struct = AlgebraicStructure.check(BPR)
    print(BPR.__name__, 'is', struct)


if __name__ == '__main__':
    galois_field_test()
    bool_polynomial_ring_test()
