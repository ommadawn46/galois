class Set:
    def __pow__(s, o):
        if not isinstance(o, int):
            raise
        if o == 0:
            return s.one()
        x = s ** (o >> 1)
        y = x * x
        if o & 1:
            y *= s
        return y

    @classmethod
    def random(cls):
        raise Exception("not implemented")

    @classmethod
    def zero(cls):
        raise Exception("not implemented")

    @classmethod
    def one(cls):
        raise Exception("not implemented")
