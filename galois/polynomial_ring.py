import random

import galois_field

import algebraic

GALOIS_POLYNOMIAL_RINGS = {}


class PolynomialRing(algebraic.Set):
    def __init__(self, coefs):
        if type(coefs) is self.__class__:
            coefs = coefs.coefs[:]
        if type(coefs) is not list:
            raise
        self.coefs = coefs

    def __str__(self):
        s = ""
        is_first = True
        for i in range(self.degree())[::-1]:
            c = self.coefs[i]
            if c == 0:
                continue
            s += (
                [" + ", ""][is_first]
                + [f"{c}", ""][c == 1 and i != 0]
                + ["x", ""][i == 0]
                + [f"^{i}", ""][i < 2]
            )
            is_first = False
        if s == "":
            return "0"
        return s

    def __repr__(self):
        return str(self)

    def __add__(s, o):
        if type(o) is not s.__class__:
            raise
        s_degree, o_degree = s.degree(), o.degree()
        coefs = [
            (s.coefs[i] if i < s_degree else 0) + (o.coefs[i] if i < o_degree else 0)
            for i in range(max(s_degree, o_degree))
        ]
        return s.__class__(coefs)

    def __neg__(s):
        coefs = []
        for c in s.coefs:
            coefs.append(-c)
        return s.__class__(coefs)

    def __sub__(s, o):
        if type(o) is not s.__class__:
            raise
        return s + (-o)

    def __mul__(s, o):
        if type(o) is not s.__class__:
            raise
        s_degree, o_degree = s.degree(), o.degree()
        coefs = [0] * (s_degree + o_degree - 1)
        for i in range(s_degree):
            if s.coefs[i] == 0:
                continue
            for j in range(o_degree):
                coefs[i + j] += s.coefs[i] * o.coefs[j]
        return s.__class__(coefs)

    def _div_mod(s, o):
        if type(o) is not s.__class__:
            raise
        q = s.__class__([0])
        r = s
        while r.degree() >= o.degree():
            e = r.degree() - o.degree()
            c = r.leading_coef() / o.leading_coef()
            p = s.__class__([0] * e + [c])
            q += p
            r -= p * o
        return q, r

    def __floordiv__(s, o):
        q, _ = s._div_mod(o)
        return q

    def __mod__(s, o):
        _, r = s._div_mod(o)
        return r

    def __truediv__(s, o):
        # undefined
        raise

    def __eq__(s, o):
        if type(o) is not s.__class__:
            raise
        if s.degree() != o.degree():
            return False
        for i in range(s.degree()):
            if s.coefs[i] != o.coefs[i]:
                return False
        return True

    def degree(self):
        for i in range(len(self.coefs))[::-1]:
            if self.coefs[i] != 0:
                return i + 1
        return 0

    def leading_coef(self):
        d = self.degree()
        if d <= 0:
            return None
        return self.coefs[d - 1]


class RealPolynomialRing(PolynomialRing):
    def __init__(self, coefs):
        super().__init__(coefs)
        for c in self.coefs:
            if not (type(c) is int or type(c) is float):
                raise

    @classmethod
    def random(cls):
        return cls(
            [random.randint(-1 << 16, 1 << 16) for _ in range(random.randint(1, 100))]
        )

    @classmethod
    def zero(cls):
        return cls([0])

    @classmethod
    def one(cls):
        return cls([1])


class GPR(PolynomialRing):
    GF = None

    def __init__(self, coefs):
        super().__init__(coefs)
        for i in range(len(self.coefs)):
            c = self.coefs[i]
            if type(c) is not self.GF:
                self.coefs[i] = self.GF(c)

    def __repr__(self):
        return f"{self.__class__.__name__}({self})"

    def __hash__(self):
        return (self.__class__, self.GF.p, tuple(c.v for c in self.coefs)).__hash__()

    @classmethod
    def from_n(cls, n):
        coefs = []
        while n > 0:
            coefs.append(cls.GF(n))
            n //= cls.GF.p
        return cls(coefs)

    @classmethod
    def gen_irreducible_poly(cls, degree):
        n = cls.GF.p ** degree
        for n in range(n, n * degree - 1):
            poly = cls.from_n(n)
            if is_irreducible_poly(poly):
                return poly
        return None

    @classmethod
    def random(cls):
        return cls([cls.GF.random() for _ in range(random.randint(1, 100))])

    @classmethod
    def zero(cls):
        return cls([cls.GF.zero()])

    @classmethod
    def one(cls):
        return cls([cls.GF.one()])


def GaloisPolynomialRing(p):
    if p in GALOIS_POLYNOMIAL_RINGS:
        return GALOIS_POLYNOMIAL_RINGS[p]
    else:
        galois_polynomial_ring = type(f"GaloisPolynomialRing[{p.p}]", (GPR,), {})
        galois_polynomial_ring.GF = p
        GALOIS_POLYNOMIAL_RINGS[p] = galois_polynomial_ring
        return galois_polynomial_ring


def is_irreducible_poly(poly):
    p, d = poly.GF.p, poly.degree()
    for n in range(2, p ** (d - 1)):
        d_poly = poly.__class__.from_n(n)
        if poly % d_poly == poly.zero():
            return False
    return True