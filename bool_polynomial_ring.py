import galois_field
import random

GF = galois_field.GaloisField(2)
F, T = GF(0), GF(1)

class BooleanPolynomialRing:
    def __init__(self, coefs):
        if type(coefs) is type(self):
            coefs = coefs.coefs[:]
        self.coefs = [(F if c == 0 else T) for c in coefs]

    def __str__(self):
        s = []
        for i in range(self.degree()):
            if self.coefs[i] == T:
                if i == 0:
                    s.append(f'1')
                elif i == 1:
                    s.append(f'x')
                else:
                    s.append(f'x^{i}')
        if len(s) <= 0:
            return '0'
        return ' + '.join(s[::-1])

    def __repr__(self):
        return str(self)

    def __add__(s, o):
        if type(s) is not type(o):
            raise
        coefs = [0] * max(s.degree(), o.degree())
        for i in range(len(coefs)):
            coefs[i] = F
            if i < s.degree():
                coefs[i] += s.coefs[i]
            if i < o.degree():
                coefs[i] += o.coefs[i]
        return s.__class__(coefs)

    def __sub__(s, o):
        return s + o

    def __mul__(s, o):
        if type(s) is not type(o):
            raise
        coefs = []
        for i in range(s.degree()):
            if s.coefs[i] != T:
                continue
            for j in range(o.degree()):
                if o.coefs[j] == T:
                    if i + j + 1 > len(coefs):
                        coefs += [F] * (i + j + 1 - len(coefs))
                    coefs[i + j] += T
        return s.__class__(coefs)

    def _div_mod(s, o):
        if type(s) is not type(o):
            raise
        q = s.__class__([0])
        r = s
        while r.degree() >= o.degree():
            e = r.degree() - o.degree()
            c = r.leading_coef() / o.leading_coef()
            p = s.__class__([0]*e + [c])
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
        return s // o

    def __eq__(s, o):
        if type(s) is not type(o):
            raise
        for i in range(max(s.degree(), o.degree())):
            if i < s.degree() and i < o.degree():
                if s.coefs[i] != o.coefs[i]:
                    return False
            else:
                if (i >= s.degree() and o.coefs[i] == T) or \
                   (i >= o.degree() and s.coefs[i] == T):
                        return False
        return True

    def degree(self):
        for i in range(len(self.coefs))[::-1]:
            if self.coefs[i] == 1:
                return i+1
        return 0

    def leading_coef(self):
        d = self.degree()
        if d <= 0:
            return None
        return self.coefs[d-1]

    @classmethod
    def random(cls):
        coefs = [0] * 100
        for i in range(len(coefs)):
            coefs[i] = F if random.random() < 0.5 else T
        return cls(coefs)

    @classmethod
    def zero(cls):
        return cls([0])

    @classmethod
    def one(cls):
        return cls([1])
