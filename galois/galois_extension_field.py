import random

import util
import galois_field
import polynomial_ring

GALOIS_EXTENSION_FIELDS = {}


class GEF(galois_field.GF):
    p = 0

    def __init__(self, v):
        if type(v) is not type(self.p):
            v = type(self.p)(v)
        super().__init__(v)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.v})"

    @classmethod
    def random(cls):
        return cls(cls.p.random() % cls.p)

    @classmethod
    def zero(cls):
        return cls(cls.p.zero())

    @classmethod
    def one(cls):
        return cls(cls.p.one())


def GaloisExtensionField(p):
    if p in GALOIS_EXTENSION_FIELDS:
        return GALOIS_EXTENSION_FIELDS[p]
    else:
        galois_extension_field = type(f"GaloisExtensionField[{p}]", (GEF,), {})
        galois_extension_field.p = p
        GALOIS_EXTENSION_FIELDS[p] = galois_extension_field
        return galois_extension_field
