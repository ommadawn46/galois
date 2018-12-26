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


def calc_crc(data, width, poly_value, init_value, reflect_in, reflect_out, xor_output):
    byte_n = width // 8

    new_data = bytearray(data) + bytearray(b"\x00" * byte_n)
    init_data = init_value.to_bytes(byte_n, "big")
    for i in range(byte_n):
        new_data[i] ^= init_data[i]

    poly_data = b"\x01" + poly_value.to_bytes(byte_n, "big")
    i_poly = GPR(bytes_to_coefs(poly_data))
    GEF = galois_extension_field.GaloisExtensionField(i_poly)

    crc_poly = GEF(bytes_to_coefs(new_data, revese=reflect_in))
    crc_bits = crc_poly.v.coefs[:width]

    out = "".join(map(lambda x: str(x.v), crc_bits[::-1]))
    out = "0" * (width - len(out)) + out

    if reflect_out:
        out = out[::-1]

    return (int(out, 2) ^ xor_output).to_bytes(byte_n, "big")


class TestCRC(unittest.TestCase):
    def test_crc(self):
        tests = [
            {
                "name": "CRC8",
                "data": b"123456789",
                "width": 8,
                "poly_value": 0x07,
                "init_value": 0x00,
                "reflect_in": False,
                "reflect_out": False,
                "xor_output": 0x00,
                "check": b"\xF4",
            },
            {
                "name": "CRC16_CCITT-FALSE",
                "data": b"123456789",
                "width": 16,
                "poly_value": 0x1021,
                "init_value": 0xFFFF,
                "reflect_in": False,
                "reflect_out": False,
                "xor_output": 0x0000,
                "check": b"\x29\xB1",
            },
            {
                "name": "CRC16_ARC",
                "data": b"123456789",
                "width": 16,
                "poly_value": 0x8005,
                "init_value": 0x0000,
                "reflect_in": True,
                "reflect_out": True,
                "xor_output": 0x0000,
                "check": b"\xbb\x3d",
            },
            {
                "name": "CRC32",
                "data": b"123456789",
                "width": 32,
                "poly_value": 0x04C11DB7,
                "init_value": 0xFFFFFFFF,
                "reflect_in": True,
                "reflect_out": True,
                "xor_output": 0xFFFFFFFF,
                "check": b"\xcb\xf4\x39\x26",
            },
            {
                "name": "CRC32_Bzip2",
                "data": b"123456789",
                "width": 32,
                "poly_value": 0x04C11DB7,
                "init_value": 0xFFFFFFFF,
                "reflect_in": False,
                "reflect_out": False,
                "xor_output": 0xFFFFFFFF,
                "check": b"\xfc\x89\x19\x18",
            },
        ]

        print()
        for test in tests:
            crc = calc_crc(
                test["data"],
                test["width"],
                test["poly_value"],
                test["init_value"],
                test["reflect_in"],
                test["reflect_out"],
                test["xor_output"],
            )

            self.assertEqual(crc, test["check"])
            print(f"{test['name']}({test['data']}) = {crc}")
