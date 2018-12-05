import galois_field
import random

GF = galois_field.GaloisField(2)

class BooleanPolynomialRing:
    def __init__(self, coefs):
        self.coefs = [(GF(0) if c == 0 else GF(1)) for c in coefs]

    def __str__(self):
        s = []
        for i in range(len(self.coefs)):
            if self.coefs[i] == GF(1):
                if i == 0:
                    s.append(f'1')
                elif i == 1:
                    s.append(f'x')
                else:
                    s.append(f'x^{i}')
        return ' + '.join(s[::-1])

    def __repr__(self):
        return str(self)

    def __add__(s, o):
        if type(s) is not type(o):
            raise
        coefs = [0] * max(len(s.coefs), len(o.coefs))
        for i in range(len(coefs)):
            coefs[i] = GF(0)
            if i < len(s.coefs):
                coefs[i] += s.coefs[i]
            if i < len(o.coefs):
                coefs[i] += o.coefs[i]
        return s.__class__(coefs)

    def __sub__(s, o):
        return s + o

    def __mul__(s, o):
        if type(s) is not type(o):
            raise
        coefs = []
        for i in range(len(s.coefs)):
            if s.coefs[i] != GF(1):
                continue
            for j in range(len(o.coefs)):
                if o.coefs[j] == GF(1):
                    if i + j + 1 > len(coefs):
                        coefs += [GF(0)] * (i + j + 1 - len(coefs))
                    coefs[i + j] += GF(1)
        return s.__class__(coefs)

    def __floordiv__(s, o):
        # not defined
        raise

    def __truediv__(s, o):
        return s.__floordiv__(o)

    def __eq__(s, o):
        if type(s) is not type(o):
            raise
        for i in range(max(len(s.coefs), len(o.coefs))):
            if i < len(s.coefs) and i < len(o.coefs):
                if s.coefs[i] != o.coefs[i]:
                    return False
            else:
                if (i >= len(s.coefs) and o.coefs[i] == GF(1)) or \
                   (i >= len(o.coefs) and s.coefs[i] == GF(1)):
                        return False
        return True

    @classmethod
    def random(cls):
        coefs = [0] * 100
        for i in range(len(coefs)):
            coefs[i] = GF(0) if random.random() < 0.5 else GF(1)
        return cls(coefs)

    @classmethod
    def zero(cls):
        return cls([0])

    @classmethod
    def one(cls):
        return cls([1])
