import random
from enum import IntEnum, auto

import prime_number
import matrix
import galois_field
import polynomial_ring
import galois_extension_field


def is_group(A):
    a, b, c = A.random(), A.random(), A.random()
    try:
        return all([a + (b + c) == (a + b) + c, a + A.zero() == a, a - a == A.zero()])
    except:
        return False


def is_abelian_group(A):
    a, b = A.random(), A.random()
    try:
        return a + b == b + a
    except:
        return False


def is_ring(A):
    a, b, c = A.random(), A.random(), A.random()
    try:
        return all(
            [
                a * (b * c) == (a * b) * c,
                a * (b + c) == a * b + a * c,
                (a + b) * c == a * c + b * c,
            ]
        )
    except:
        return False


def is_commutative_ring(A):
    a, b = A.random(), A.random()
    try:
        return a * b == b * a
    except:
        return False


def is_integral_domain(A):
    a = A.random()
    try:
        return a * A.one() == a and a * A.zero() == A.zero()
    except:
        return False


def is_field(A):
    a = A.random()
    while a == A.zero():
        a = A.random()
    try:
        return a * (A.one() / a) == A.one()
    except:
        return False


class AlgebraicStructure(IntEnum):
    SET = auto()
    GROUP = auto()
    ABELIAN_GROUP = auto()
    RING = auto()
    COMMUTATIVE_RING = auto()
    INTEGRAL_DOMAIN = auto()
    FIELD = auto()

    @classmethod
    def check(cls, A, try_n=3):
        def try_repeat(f):
            return all([f(A) for _ in range(try_n)])

        if not try_repeat(is_group):
            return cls.SET

        if not try_repeat(is_abelian_group):
            return cls.GROUP

        if not try_repeat(is_ring):
            return cls.ABELIAN_GROUP

        if not try_repeat(is_commutative_ring):
            return cls.RING

        if not try_repeat(is_integral_domain):
            return cls.COMMUTATIVE_RING

        if not try_repeat(is_field):
            return cls.INTEGRAL_DOMAIN

        return cls.FIELD


def galois_field_test():
    p = prime_number.next_prime(random.randint(1 << 15, 1 << 16))
    GF = galois_field.GaloisField(p)
    struct = AlgebraicStructure.check(GF)
    print(GF.__name__, "is", struct)


def real_polynomial_ring_test():
    RPR = polynomial_ring.RealPolynomialRing
    struct = AlgebraicStructure.check(RPR)
    print(RPR.__name__, "is", struct)


def galois_polynomial_ring_test():
    p = prime_number.next_prime(random.randint(1 << 15, 1 << 16))
    GF = galois_field.GaloisField(p)
    GPR = polynomial_ring.GaloisPolynomialRing(GF)
    struct = AlgebraicStructure.check(GPR)
    print(GPR.__name__, "is", struct)


def galois_extension_field_test():
    p = 2
    GF = galois_field.GaloisField(p)
    GPR = polynomial_ring.GaloisPolynomialRing(GF)
    i_poly = polynomial_ring.generate_irreducible_polynomial(GPR, 8)
    GEF = galois_extension_field.GaloisExtensionField(i_poly)
    struct = AlgebraicStructure.check(GEF)
    print(GEF.__name__, "is", struct)


def matrix_ring_test():
    MR = matrix.MatrixRing
    struct = AlgebraicStructure.check(MR)
    print(MR.__name__, "is", struct)


def matrix_multi_group_test():
    MMG = matrix.MatrixMultiGroup
    struct = AlgebraicStructure.check(MMG)
    print(MMG.__name__, "is", struct)


if __name__ == "__main__":
    galois_field_test()
    real_polynomial_ring_test()
    galois_polynomial_ring_test()
    galois_extension_field_test()
    matrix_ring_test()
    matrix_multi_group_test()
