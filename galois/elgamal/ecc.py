import galois_field
import elliptic_curve
import random

# Secp256k1
p = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1
GF = galois_field.GaloisField(p)
rand = lambda: random.randint(0, p-1)

a, b = 0x0, 0x7
curve = elliptic_curve.EllipticCurve(GF(a), GF(b))
Point = elliptic_curve.EllipticCurvePoint(curve)

p_x = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
p_y = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
G = Point(GF(p_x), GF(p_y))

def gen_key_pair():
    x = rand()
    P = x * G
    return x, P

def encrypt(m, P):
    r = rand()
    if isinstance(m, bytes):
        m = int.from_bytes(m, 'big')
    return r*G, r*P + m*G

def decrypt(c1, c2, x):
    return c2 - x*c1