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
        def do_test(test):
            print()
            input_cls, want = test["input_cls"], test["want"]
            got = algebraic.Structure.check(input_cls)

            print(f"{input_cls.__name__} is", got)
            self.assertEqual(got, want)

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
            {"input_cls": GFp, "want": algebraic.Structure.FIELD},
            {"input_cls": GpPR, "want": algebraic.Structure.INTEGRAL_DOMAIN},
            {"input_cls": GEF, "want": algebraic.Structure.FIELD},
            {"input_cls": GEPR, "want": algebraic.Structure.INTEGRAL_DOMAIN},
            {
                "input_cls": polynomial_ring.PolynomialRing(int),
                "want": algebraic.Structure.INTEGRAL_DOMAIN,
            },
            {
                "input_cls": bits_galois_field.BitsGaloisField,
                "want": algebraic.Structure.FIELD,
            },
            {"input_cls": matrix.MatrixRing, "want": algebraic.Structure.RING},
            {
                "input_cls": matrix.MatrixMultiGroup,
                "want": algebraic.Structure.GROUP,
            },
        ]

        for test in tests:
            with self.subTest():
                do_test(test)
