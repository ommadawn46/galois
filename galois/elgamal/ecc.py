import random

import elliptic_curve
import galois_field
import util

# Secp256k1
p = 2 ** 256 - 2 ** 32 - 2 ** 9 - 2 ** 8 - 2 ** 7 - 2 ** 6 - 2 ** 4 - 1
GF = galois_field.GaloisField(p)

a, b = 0x0, 0x7
curve = elliptic_curve.EllipticCurve(GF(a), GF(b))
Point = elliptic_curve.EllipticCurvePoint(curve)

G_x = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
G_y = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
G = Point(GF(G_x), GF(G_y))

n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

message_shift = 8


def rand():
    return random.randint(1, n - 1)


def gen_key_pair():
    x = rand()
    P = x * G
    return x, P


def message_to_point(m):
    if isinstance(m, bytes):
        m = int.from_bytes(m, "big")

    m <<= message_shift
    for i in range(1 << message_shift):
        x = m + i
        z = curve.right(x).v
        y = util.sqrt_mod(z, p)
        if y != 0:
            return Point(GF(x), GF(y))


def point_to_message(p):
    m = p.x.v >> message_shift
    byte_n = (m.bit_length() - 1) // 8 + 1
    return m.to_bytes(byte_n, "big")


def encrypt_point(M, P):
    r = rand()
    return r * G, r * P + M


def decrypt_point(c1, c2, x):
    return c2 - x * c1


def encrypt(m, P):
    M = message_to_point(m)
    return encrypt_point(M, P)


def decrypt(c1, c2, x):
    M = decrypt_point(c1, c2, x)
    return point_to_message(M)
