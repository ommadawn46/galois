def extgcd(x, y):
    # a*x + b*x = c
    a0, b0, c0 = 1, 0, x
    a1, b1, c1 = 0, 1, y
    while c1 != 0:
        q, r = c0//c1, c0%c1
        at, bt, ct = a1, b1, c1
        a1, b1, c1 = a0-a1*q, b0-b1*q, r
        a0, b0, c0 = at, bt, ct
    return c0, a0, b0

def modinv(a, n):
    g, x, y = extgcd(a, n)
    if g != 1:
        raise
    else:
        return x % n
