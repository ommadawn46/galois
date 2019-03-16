# Euler's criterion
def legendre_symbol(a, p):
    symbol = pow(a, (p - 1) // 2, p)
    if symbol == p - 1:
        return -1
    return symbol


# Tonelli–Shanks algorithm
def sqrt_mod(a, p):
    if a == 0 or legendre_symbol(a, p) != 1:
        return 0
    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)
    if p % 8 == 5:
        if pow(a, (p - 1) // 4, p) == 1:
            return pow(a, (p + 3) // 8, p)
        else:
            return (pow(2, (p - 1) // 4, p) * pow(a, (p + 3) // 8, p)) % p

    q = p - 1
    s = 0
    while q & 1 == 0:
        q >>= 1
        s += 1

    z = 2
    while legendre_symbol(z, p) != -1:
        z += 1

    m = s
    c = pow(z, q, p)
    t = pow(a, q, p)
    r = pow(a, (q + 1) // 2, p)

    while t != 1:
        t2 = t
        i = 0
        while t2 != 1 and i < m:
            t2 = pow(t2, 2, p)
            i += 1

        b = pow(c, 2 ** (m - i - 1), p)
        m = i
        c = (b * b) % p
        t = (t * c) % p
        r = (r * b) % p

    return r
