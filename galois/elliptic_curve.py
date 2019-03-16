import math
import random
from fractions import Fraction

import algebraic

ELLIPTIC_CURVES = {}


class Point(algebraic.Set):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    def __add__(s, o):
        x1, x2, y1, y2 = s.x, o.x, s.y, o.y
        a = s.curve.a

        if x1 is None and y1 is None:
            return o
        if x2 is None and y2 is None:
            return s

        if x1 == x2 and y1 == -y2:
            return s.zero()

        if x1 == x2 and y1 == y2:
            if y1 is None:
                return s.zero()
            l = (x1 * x1 * 3 + a) / (y1 * 2)
        else:
            l = (y2 - y1) / (x2 - x1)
            
        x3 = l * l - x1 - x2
        y3 = l * (x1 - x3) - y1

        p = s.__class__(x3, y3)
        if not s.curve.on_curve(p):
            raise
        return p

    def __sub__(s, o):
        return s + (-o)

    def __neg__(s):
        y = None if s.y is None else -s.y
        return s.__class__(s.x, y)

    def __mul__(s, o):
        if not isinstance(o, int):
            raise
        if o == 0:
            return s.zero()
        if o == 1:
            return s
        x = s * (o >> 1)
        y = x + x
        if o & 1:
            y += s
        return y

    def __eq__(s, o):
        return s.x == o.x and s.y == o.y

    @classmethod
    def zero(cls):
        return cls(None, None)

    @classmethod
    def random(cls):
        x = Fraction(0)
        y = Fraction(math.sqrt(cls.curve.b))
        p = cls(x, y) * random.randint(0, 100)
        if random.random() < 0.5:
            return p
        else:
            return -p


class EllipticCurve:
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __str__(self):
        return f"y*y = x**3 + {self.a}*x + {self.b}"

    def __repr__(self):
        return f"{self.__class__.__name__}(y*y = x**3 + {self.a}*x + {self.b})"

    def left(self, y):
        return y * y

    def right(self, x):
        return x ** 3 + self.a * x + self.b

    def on_curve(self, p):
        return self.left(p.y) == self.right(p.x)


def EllipticCurvePoint(curve):
    if curve in ELLIPTIC_CURVES:
        return ELLIPTIC_CURVES[curve]
    else:
        point = type(f"Point[{curve}]", (Point,), {})
        point.curve = curve
        ELLIPTIC_CURVES[curve] = point
        return point
