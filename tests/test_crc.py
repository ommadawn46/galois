import unittest

import pathmagic

with pathmagic.context():
    import crc


class TestCRC(unittest.TestCase):
    def test_crc(self):
        def do_test(test):
            print()
            crc_code = crc.calc(
                test["data"],
                test["width"],
                test["poly_value"],
                test["init_value"],
                test["reflect_in"],
                test["reflect_out"],
                test["xor_output"],
            )

            print(f"{test['name']}({test['data']}) = {crc_code}")
            self.assertEqual(crc_code, test["check"])

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

        for test in tests:
            with self.subTest():
                do_test(test)
