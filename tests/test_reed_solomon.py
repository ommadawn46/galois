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
    def test_compare_naive_and_bits(self):
        def do_test(test):
            print()
            input_data, n, k = test["input_data"], test["n"], test["k"]

            naive_rs = reed_solomon.NaiveRS(n, k)
            bits_rs = reed_solomon.BitsRS(n, k)

            naive_code = naive_rs.encode(input_data)
            bits_code = bits_rs.encode(input_data)

            self.assertEqual(naive_code, bits_code)
            print(
                f"{reed_solomon.NaiveRS.__name__}.encode({input_data}) = "
                f"{reed_solomon.BitsRS.__name__}.encode({input_data}) = "
                f"{naive_code}"
            )

        tests = [
            {"input_data": b"Puzzle", "n": 10, "k": 6},
            {"input_data": b"Blackjack", "n": 26, "k": 9},
            {"input_data": b"ReedSolomonEncoding", "n": 26, "k": 19},
        ]

        for test in tests:
            with self.subTest():
                do_test(test)

    def test_reed_solomon(self):
        def do_test(test):
            print()
            RS, input_data, n, k = (
                test["codec"],
                test["input_data"],
                test["n"],
                test["k"],
            )
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

        tests = [
            {
                "codec": reed_solomon.NaiveRS,
                "input_data": b"Puzzle",
                "n": 10,
                "k": 6,
            },
            {
                "codec": reed_solomon.NaiveRS,
                "input_data": b"Blackjack",
                "n": 26,
                "k": 9,
            },
            {
                "codec": reed_solomon.NaiveRS,
                "input_data": b"ReedSolomonEncoding",
                "n": 26,
                "k": 19,
            },
            {
                "codec": reed_solomon.BitsRS,
                "input_data": (
                    b"He was an old man who fished a"
                    b"lone in a skiff in the Gulf St"
                ),
                "n": 100,
                "k": 60,
            },
            {
                "codec": reed_solomon.BitsRS,
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
                "codec": reed_solomon.BitsRS,
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
            {
                "codec": reed_solomon.ModuloRS,
                "input_data": b"The old man was thin and gaunt",
                "n": 64,
                "k": 30,
            },
            {
                "codec": reed_solomon.ModuloRS,
                "input_data": b"with deep wrinkles in the back",
                "n": 72,
                "k": 30,
            },
            {
                "codec": reed_solomon.ModuloRS,
                "input_data": b"of his neck. The brown blotche",
                "n": 80,
                "k": 30,
            },
        ]

        for test in tests:
            with self.subTest():
                do_test(test)
