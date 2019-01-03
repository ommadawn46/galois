import random

import algebraic
import galois_field

global CURRENT_VARCHAR
CURRENT_VARCHAR = ord("a")
POLYNOMIAL_RINGS = {}


class PR(algebraic.Set):
    def __init__(self, coefs):
        if isinstance(coefs, self.__class__):
            coefs = coefs.coefs[:]
        if not isinstance(coefs, list):
            coefs = [coefs]
        for i in range(len(coefs)):
            c = coefs[i]
            if not isinstance(c, self.coef_cls):
                coefs[i] = self.coef_cls(c)
        self.coefs = coefs
        self.degree = self._degree()

    def __str__(self):
        s = ""
        is_first = True
        for i in range(self.degree)[::-1]:
            c = self[i]
            c_is_algset = isinstance(c, algebraic.Set)
            if c == self.coef_zero:
                continue
            s += (
                [" + ", ""][is_first]
                + [f"({c})" if c_is_algset and i != 0 else f"{c}", ""][
                    c == self.coef_one and i != 0
                ]
                + [f"{self.VARCHAR}", ""][i == 0]
                + [f"^{i}", ""][i < 2]
            )
            is_first = False
        if s == "":
            return f"{self.coef_zero}"
        return s

    def __repr__(self):
        return f"{self.__class__.__name__}({self})"

    def __hash__(self):
        return (self.__class__, self.coef_cls, tuple(self.coefs)).__hash__()

    def __add__(s, o):
        s._type_check(o, "+")
        s_degree, o_degree = s.degree, o.degree
        coefs = [
            (s[i] if i < s_degree else s.coef_zero)
            + (o[i] if i < o_degree else o.coef_zero)
            for i in range(max(s_degree, o_degree))
        ]
        return s.__class__(coefs)

    def __neg__(s):
        coefs = []
        for c in s.coefs:
            coefs.append(-c)
        return s.__class__(coefs)

    def __sub__(s, o):
        s._type_check(o, "-")
        return s + (-o)

    def __mul__(s, o):
        s._type_check(o, "*")
        coefs = [s.coef_zero] * (s.degree + o.degree - 1)
        for i in range(s.degree):
            if s[i] == s.coef_zero:
                continue
            for j in range(o.degree):
                coefs[i + j] += s[i] * o[j]
        return s.__class__(coefs)

    def _div_mod(s, o):
        q = s.zero()
        r = s
        while r.degree >= o.degree:
            e = r.degree - o.degree
            c = r.leading_coef() / o.leading_coef()
            p = s.__class__([s.coef_zero] * e + [c])
            q += p
            r -= p * o
        return q, r

    def __floordiv__(s, o):
        s._type_check(o, "//")
        q, _ = s._div_mod(o)
        return q

    def __mod__(s, o):
        s._type_check(o, "%")
        _, r = s._div_mod(o)
        return r

    def __truediv__(s, o):
        # undefined
        raise Exception("undefined")

    def __eq__(s, o):
        s._type_check(o, "==")
        if s.degree != o.degree:
            return False
        for i in range(s.degree):
            if s[i] != o[i]:
                return False
        return True

    def __getitem__(self, idx):
        return self.coefs[idx]

    def __setitem__(self, idx, val):
        self.coefs[idx] = val
        self.degree = self._degree()

    def __iter__(self):
        return iter(self.coefs)

    def __len__(self):
        return self.degree

    def _type_check(s, o, operand):
        if not isinstance(o, s.__class__):
            raise TypeError(
                f"unsupported operand type(s) for {operand}: "
                f"'{s.__class__.__name__}' and '{type(o).__name__}'"
            )

    def _degree(self):
        d = 0
        length = len(self.coefs)
        for i in range(length)[::-1]:
            if self[i] != self.coef_zero:
                d = i + 1
                break
        if d < length:
            self.coefs = self.coefs[:d]
        return d

    def leading_coef(self):
        d = self.degree
        if d <= 0:
            return None
        return self[d - 1]

    def apply(s, x):
        r = s.coef_zero
        for d in range(s.degree):
            r += s[d] * (x ** d)
        return r

    def is_irreducible_poly(self):
        p, d = self.coef_cls.p, self.degree
        for n in range(2, p ** (d - 1)):
            d_poly = from_n(self.__class__, n)
            if self % d_poly == self.zero():
                return False
        return True

    def is_primitive_poly(self, degree):
        if not self.is_irreducible_poly():
            return False
        p = self.coef_cls.p ** degree
        divs = [d for d in range(1, p - 1) if (p - 1) % d == 0]

        x = self.__class__([self.coef_zero, self.coef_one])
        for d in divs:
            if (x ** d) % self == self.one():
                return False
        return True

    @classmethod
    def gen_primitive_poly(cls, degree):
        if not issubclass(cls.coef_cls, galois_field.GF):
            raise TypeError(
                f"generating a primitive poly is possible only with "
                f"{galois_field.GF.__name__} coefs"
            )
        n = cls.coef_cls.p ** degree
        for n in range(n, n * cls.coef_cls.p):
            poly = from_n(cls, n)
            if poly.is_primitive_poly(degree):
                return poly
        return None

    @classmethod
    def random(cls):
        if issubclass(cls.coef_cls, algebraic.Set):
            return cls(
                [cls.coef_cls.random() for _ in range(random.randint(1, 16))]
            )
        if issubclass(cls.coef_cls, (int, float)):
            return cls(
                [
                    random.randint(-1 << 16, 1 << 16)
                    for _ in range(random.randint(1, 100))
                ]
            )
        raise TypeError(f"unsupported coef class: {cls.coef_cls.__name__}")

    @classmethod
    def zero(cls):
        return cls(cls.coef_zero)

    @classmethod
    def one(cls):
        return cls(cls.coef_one)


def PolynomialRing(p):
    if p in POLYNOMIAL_RINGS:
        return POLYNOMIAL_RINGS[p]
    else:
        global CURRENT_VARCHAR
        polynomial_ring = type(f"PolynomialRing[{p.__name__}]", (PR,), {})
        polynomial_ring.coef_cls = p
        polynomial_ring.coef_zero = (
            p.zero() if issubclass(p, algebraic.Set) else 0
        )
        polynomial_ring.coef_one = (
            p.one() if issubclass(p, algebraic.Set) else 1
        )

        polynomial_ring.VARCHAR = chr(CURRENT_VARCHAR)
        CURRENT_VARCHAR += 1

        POLYNOMIAL_RINGS[p] = polynomial_ring
        return polynomial_ring


def from_n(cls, n):
    coefs = []
    while n > 0:
        coefs.append(cls.coef_cls(n))
        n //= cls.coef_cls.p
    return cls(coefs)
