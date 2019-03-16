import random


def is_composite(a, d, n):
    y = pow(a, d, n)
    if y == 1:
        return False
    t = d
    while t != n - 1 and y != n - 1:
        y = (y * y) % n
        t *= 2
    return y != n - 1 and t != d


# Miller–Rabin primality test
def probably_prime(n, k=16):
    n = abs(n)
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False

    d = n - 1
    while d % 2 == 0:
        d //= 2

    for _ in range(k):
        a = random.randint(1, n - 1)
        if is_composite(a, d, n):
            return False
    return True


def next_prime(n):
    n += 1 + (n % 2 != 0)
    while not probably_prime(n):
        n += 2
    return n
