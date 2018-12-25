import sys
import os

path = os.path.join(os.path.dirname(__file__), "../galois")
sys.path.append(path)

import unittest

from galois import galois_field
from galois import polynomial_ring
from galois import galois_extension_field


p = 2
GF = galois_field.GaloisField(p)
GPR = polynomial_ring.GaloisPolynomialRing(GF)


def bytes_to_coefs(data, revese=False):
    coefs = []
    for b in data:
        word_coefs = []
        for i in range(8):
            word_coefs.append(b % 2)
            b //= 2
        if revese:
            word_coefs = word_coefs[::-1]
        coefs = word_coefs + coefs
    return coefs


def calc_crc(
    data,
    width=32,
    poly_value=0x04C11DB7,
    init_value=0xFFFFFFFF,
    reflect_in=True,
    reflect_out=True,
    xor_output=0xFFFFFFFF,
):
    byte_n = width // 8

    poly_data = b"\x01" + poly_value.to_bytes(byte_n, "big")
    i_poly = GPR(bytes_to_coefs(poly_data))
    GEF = galois_extension_field.GaloisExtensionField(i_poly)

    new_data = bytearray(data) + bytearray(b"\x00" * byte_n)
    init_data = init_value.to_bytes(byte_n, "big")
    for i in range(byte_n):
        new_data[i] ^= init_data[i]

    crc_poly = GEF(bytes_to_coefs(new_data, revese=reflect_in))
    crc_bits = crc_poly.v.coefs[:width]

    out = "".join(map(lambda x: str(x.v), crc_bits[::-1]))
    out = "0" * (width - len(out)) + out

    if reflect_out:
        out = out[::-1]

    return (int(out, 2) ^ xor_output).to_bytes(byte_n, "big")


class TestCRC(unittest.TestCase):
    def test_crc16(self):
        input = b"123456789"
        want = b"\xbb\x3d"
        got = calc_crc(
            input, width=16, poly_value=0x8005, init_value=0x0000, xor_output=0x0000
        )

        self.assertEqual(got, want)
        print(f"\nCRC16({input}) = {got}")

    def test_crc32(self):
        input = b"123456789"
        want = b"\xcb\xf4\x39\x26"
        got = calc_crc(input)

        self.assertEqual(got, want)
        print(f"\nCRC32({input}) = {got}")

    def test_crc32_bzip2(self):
        input = b"123456789"
        want = b"\xfc\x89\x19\x18"
        got = calc_crc(input, reflect_in=False, reflect_out=False)

        self.assertEqual(got, want)
        print(f"\nCRC32_Bzip2({input}) = {got}")
