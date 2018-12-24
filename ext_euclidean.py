import algebraic


def extgcd(x, y):
    zero, one = 0, 1
    if issubclass(type(x), algebraic.Set) and issubclass(type(y), algebraic.Set):
        zero, one = x.zero(), x.one()
    a0, b0, c0 = one, zero, x
    a1, b1, c1 = zero, one, y
    while c1 != zero:
        q, r = c0 // c1, c0 % c1
        a0, b0, c0, a1, b1, c1 = a1, b1, c1, a0 - a1 * q, b0 - b1 * q, r
    return c0, a0, b0


def modinv(a, n):
    one = 1
    if issubclass(type(a), algebraic.Set) and issubclass(type(n), algebraic.Set):
        one = a.one()
    g, x, y = extgcd(a, n)
    if g != one:
        raise
    else:
        return x % n
