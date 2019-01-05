import random
import unittest

import pathmagic

with pathmagic.context():
    import algebraic
    import galois_field
    import bits_galois_field
    import matrix
    import polynomial_ring
    import util


class TestAlgebraicStructure(unittest.TestCase):
    def test_galois_field(self):
        def do_test(A, want_struct):
            print()
            got_struct = algebraic.Structure.check(A)

            print(f"{A.__name__} is", got_struct)
            self.assertEqual(got_struct, want_struct)

        p = util.next_prime(random.randint(1 << 15, 1 << 16))
        GFp = galois_field.GaloisField(p)
        GpPR = polynomial_ring.PolynomialRing(GFp)

        p = 2
        GF2 = galois_field.GaloisField(p)
        G2PR = polynomial_ring.PolynomialRing(GF2)
        primitive_poly = G2PR.gen_primitive_poly(8)
        GEF = galois_field.GaloisField(primitive_poly)
        GEPR = polynomial_ring.PolynomialRing(GEF)

        tests = [
            {"input": GFp, "want": algebraic.Structure.FIELD},
            {"input": GpPR, "want": algebraic.Structure.INTEGRAL_DOMAIN},
            {"input": GEF, "want": algebraic.Structure.FIELD},
            {"input": GEPR, "want": algebraic.Structure.INTEGRAL_DOMAIN},
            {
                "input": polynomial_ring.PolynomialRing(int),
                "want": algebraic.Structure.INTEGRAL_DOMAIN,
            },
            {
                "input": bits_galois_field.BitsGaloisField,
                "want": algebraic.Structure.FIELD,
            },
            {"input": matrix.MatrixRing, "want": algebraic.Structure.RING},
            {
                "input": matrix.MatrixMultiGroup,
                "want": algebraic.Structure.GROUP,
            },
        ]

        for test in tests:
            with self.subTest():
                do_test(test["input"], test["want"])
