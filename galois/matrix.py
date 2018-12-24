import numpy as np

import algebraic


class MatrixRing(algebraic.Set):
    def __init__(self, m):
        if type(m) is not np.ndarray:
            m = np.array(m)
        self.m = m

    def __str__(self):
        return str(self.m)

    def __repr__(self):
        return repr(self.m)

    def __add__(s, o):
        if type(s) is not type(o):
            raise
        return s.__class__(s.m + o.m)

    def __sub__(s, o):
        if type(s) is not type(o):
            raise
        return s.__class__(s.m - o.m)

    def __mul__(s, o):
        if type(s) is not type(o):
            raise
        return s.__class__(np.dot(s.m, o.m))

    def _inverse(s):
        return s.__class__(np.linalg.inv(s.m))

    def __truediv__(s, o):
        if type(s) is not type(o):
            raise
        return s * o._inverse()

    __floordiv__ = __truediv__

    def __eq__(s, o):
        if type(s) is not type(o):
            raise
        return np.allclose(s.m, o.m)

    @classmethod
    def random(cls, n=16):
        return cls(np.random.rand(n, n))

    @classmethod
    def zero(cls, n=16):
        return cls(np.zeros([n, n]))

    @classmethod
    def one(cls, n=16):
        return cls(np.eye(n))


class MatrixMultiGroup(MatrixRing):
    def __init__(self, m):
        super().__init__(m)

    def __add__(s, o):
        return super().__mul__(o)

    def __sub__(s, o):
        if type(s) is not type(o):
            raise
        return s + o._inverse()

    __mul__ = None
    __truediv__ = None
    __floordiv__ = None

    @classmethod
    def zero(cls, n=16):
        return super().one()

    one = None
