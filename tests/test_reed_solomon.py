import sys
import os

path = os.path.join(os.path.dirname(__file__), "../galois")
sys.path.append(path)

import random
import unittest
from encoding import reed_solomon as rs


class TestReedSolomons(unittest.TestCase):
    def test_reed_solomon(self):
        tests = [
            {"input_data": b"Puzzle", "n": 10, "k": 6},
            {"input_data": b"Blackjack", "n": 26, "k": 9},
            {"input_data": b"ReedSolomonEncoding", "n": 26, "k": 19},
        ]

        print()
        for test in tests:
            input_data, n, k = test["input_data"], test["n"], test["k"]

            I = rs.data_to_rs_poly(input_data)
            C = rs.encode(I, n, k)

            noise = rs.RS.zero()
            for i in range((n - k) // 2):
                gef = rs.GEF.random()
                while gef == rs.GEF.zero():
                    gef = rs.GEF.random()
                d = random.randint(1, n - 1)
                noise += rs.RS([gef]) * rs.x ** d
            noised_C = C + noise
            noised_data = rs.rs_poly_to_data(noised_C)

            decoded_I = rs.decode(noised_C, n, k)
            decoded_data = rs.rs_poly_to_data(decoded_I)

            self.assertEqual(decoded_data, input_data)

            print(f"ReedSolomon({noised_data}) = {decoded_data}")
