import random
import unittest

import pathmagic

with pathmagic.context():
    import reed_solomon


def make_noise_poly(rs, n, k):
    noise_poly = rs.RS.zero()
    for i in range((n - k) // 2):
        gef = rs.GEF.random()
        while gef == rs.GEF.zero():
            gef = rs.GEF.random()
        d = random.randint(0, n - 1)
        noise_poly += rs.RS([gef]) * rs.x ** d
    return noise_poly


class TestReedSolomon(unittest.TestCase):
    def reed_solomon_test(self, RS, tests):
        print()
        for test in tests:
            input_data, n, k = test["input_data"], test["n"], test["k"]
            rs = RS(n, k)

            I = rs.data_to_poly(input_data)
            C = rs.encode_poly(I)

            noise_poly = make_noise_poly(rs, n, k)
            noised_C = noise_poly + C

            decoded_I = rs.decode_poly(noised_C)

            print(
                f"""{RS.__name__}.decode({
                    rs.poly_to_data(noised_C)
                }) = {
                    rs.poly_to_data(decoded_I)
                }"""
            )
            self.assertEqual(I, decoded_I)

    def test_naive_reed_solomon(self):
        tests = [
            {"input_data": b"Puzzle", "n": 10, "k": 6},
            {"input_data": b"Blackjack", "n": 26, "k": 9},
            {"input_data": b"ReedSolomonEncoding", "n": 26, "k": 19},
        ]
        self.reed_solomon_test(reed_solomon.NaiveRS, tests)

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
        self.reed_solomon_test(reed_solomon.BitsRS, tests)
