from enum import IntEnum, auto


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
    def check(cls, A, try_n=5):
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
