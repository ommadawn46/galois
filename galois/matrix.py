import algebraic
import set
import copy
import random
from itertools import product

EPSILON = 1e-10


class MatrixRing(algebraic.Set):
    def __init__(self, m):
        if isinstance(m, MatrixRing):
            m = m.m
        if not isinstance(m, list):
            raise
        self.m = m
        shape, t_m = [], m
        while True:
            try:
                shape.append(len(t_m))
                t_m = t_m[0]
            except:
                break
        self.shape = tuple(shape)

    def __str__(self):
        return str(self.m)

    def __repr__(self):
        return repr(self.m)

    def __add__(s, o):
        if type(s) is not type(o):
            raise
        if s.shape != o.shape:
            raise
        m = copy.deepcopy(s.m)
        for idxs in product(*map(lambda x: range(x), s.shape)):
            sp, op, sv, ov = None, None, m, o.m
            for idx in idxs:
                sp, op, sv, ov = sv, ov, sv[idx], ov[idx]
            sp[idx] += ov
        return s.__class__(m)

    def __sub__(s, o):
        if type(s) is not type(o):
            raise
        if s.shape != o.shape:
            raise
        m = copy.deepcopy(s.m)
        for idxs in product(*map(lambda x: range(x), s.shape)):
            sp, op, sv, ov = None, None, m, o.m
            for idx in idxs:
                sp, op, sv, ov = sv, ov, sv[idx], ov[idx]
            sp[idx] -= ov
        return s.__class__(m)

    def __mul__(s, o):
        if type(s) is not type(o):
            raise
        if len(s.shape) != 2:
            raise
        if s.shape[1] != o.shape[0]:
            raise
        m = [[0] * o.shape[1] for _ in range(s.shape[0])]
        for i in range(s.shape[0]):
            for j in range(o.shape[1]):
                for k in range(o.shape[0]):
                    m[i][j] += s.m[i][k] * o.m[k][j]
        return s.__class__(m)

    def _inverse(s):
        inv_m = s.gaussian_elimination(inv=True)
        return s.__class__(inv_m)

    def __truediv__(s, o):
        if type(s) is not type(o):
            raise
        return s * o._inverse()

    __floordiv__ = __truediv__

    def __eq__(s, o):
        if type(s) is not type(o):
            raise
        for idxs in product(*map(lambda x: range(x), s.shape)):
            sp, op, sv, ov = None, None, s.m, o.m
            for idx in idxs:
                sp, op, sv, ov = sv, ov, sv[idx], ov[idx]
            is_set = isinstance(sv, set.Set)
            if is_set and sv != ov:
                return False
            if not is_set and not -EPSILON < sv - ov < EPSILON:
                return False
        return True

    def __len__(self):
        return len(self.m)

    def __getitem__(self, idx):
        return self.m[idx]

    def __setitem__(self, idx, val):
        self.m[idx] = val

    def gaussian_elimination(s, inv=False):
        m = MatrixRing(s.m[:])
        zero = m[0][0].zero() if isinstance(m[0][0], set.Set) else 0
        if inv:
            inv_m = MatrixRing.one(len(m))
        for i in range(len(m)):
            c1, j = m[i][i], i + 1
            while j < len(m) and c1 == zero:
                # pivot
                m[i], m[j] = m[j], m[i]
                if inv:
                    inv_m[i], inv_m[j] = inv_m[j], inv_m[i]
                c1, j = m[i][i], j + 1
            if c1 == zero:
                continue

            m[i] = [m[i][j] / c1 for j in range(len(m[i]))]
            if inv:
                inv_m[i] = [inv_m[i][j] / c1 for j in range(len(inv_m[i]))]
            for j in range(len(m)):
                if i == j:
                    continue
                c2 = m[j][i]
                m[j] = [m[j][k] - m[i][k] * c2 for k in range(len(m[j]))]
                if inv:
                    inv_m[j] = [
                        inv_m[j][k] - inv_m[i][k] * c2 for k in range(len(inv_m[j]))
                    ]
        if inv:
            return inv_m
        return m

    def check_rank(s):
        one = s[0][0].one() if isinstance(s[0][0], set.Set) else 1
        for i in range(len(s)):
            if s[i][i] != one:
                return i
        return len(s)

    @classmethod
    def random(cls, n=16):
        return cls([[random.random() for _ in range(n)] for _ in range(n)])

    @classmethod
    def zero(cls, n=16):
        return cls([[0] * n for _ in range(n)])

    @classmethod
    def one(cls, n=16):
        m = [[0] * n for _ in range(n)]
        for i in range(n):
            m[i][i] = 1
        return cls(m)


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
