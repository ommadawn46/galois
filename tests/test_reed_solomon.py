import random
import unittest

import pathmagic

with pathmagic.context():
    from encoding.reed_solomon import naive_rs
    from encoding.reed_solomon import bits_rs


class TestReedSolomon(unittest.TestCase):
    def test_naive_reed_solomon(self):
        tests = [
            {"input_data": b"Puzzle", "n": 10, "k": 6},
            {"input_data": b"Blackjack", "n": 26, "k": 9},
            {"input_data": b"ReedSolomonEncoding", "n": 26, "k": 19},
        ]
        self.rs_test(naive_rs.NaiveRS, tests)

    def test_bits_reed_solomon(self):
        tests = [
            {
                "input_data": (
                    b"He was an old man who fished a"
                    b"lone in a skiff in the Gulf St"
                ),
                "n": 100,
                "k": 60,
            },
            {
                "input_data": (
                    b"ream and he had gone eighty-fo"
                    b"ur days now without taking a f"
                    b"ish. In the first forty days a"
                    b" boy had been with him. But af"
                ),
                "n": 150,
                "k": 120,
            },
            {
                "input_data": (
                    b"ter forty days without a fish "
                    b"the boy's parents had told him"
                    b" that the old man was now defi"
                    b"nitely and finally salao, whic"
                    b"h is the worst form of unlucky"
                    b", and the boy had gone at thei"
                ),
                "n": 250,
                "k": 180,
            },
        ]
        self.rs_test(bits_rs.BitsRS, tests)

    def rs_test(self, RS, tests):
        print()
        for test in tests:
            input_data, n, k = test["input_data"], test["n"], test["k"]
            rs = RS(n, k)

            I = rs.data_to_poly(input_data)
            C = rs.encode_poly(I)

            noise_poly = rs.RS.zero()
            for i in range((n - k) // 2):
                gef = rs.GEF.random()
                while gef == rs.GEF.zero():
                    gef = rs.GEF.random()
                d = random.randint(1, n - 1)
                noise_poly += rs.RS([gef]) * rs.x ** d
            noised_C = C + noise_poly
            noised_data = rs.poly_to_data(noised_C)

            decoded_I = rs.decode_poly(noised_C)
            decoded_data = rs.poly_to_data(decoded_I)

            print(f"{RS.__name__}({noised_data}) = {decoded_data}")
            self.assertEqual(decoded_data, input_data)
