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
        print()

        p = util.next_prime(random.randint(1 << 15, 1 << 16))
        GF = galois_field.GaloisField(p)
        struct = algebraic.Structure.check(GF)

        print(f"{GF.__name__} is", struct)
        self.assertEqual(struct, algebraic.Structure.FIELD)

        GPR = polynomial_ring.PolynomialRing(GF)
        struct = algebraic.Structure.check(GPR)

        print(f"{GPR.__name__} is", struct)
        self.assertEqual(struct, algebraic.Structure.INTEGRAL_DOMAIN)

    def test_galois_extension_field(self):
        print()

        p = 2
        GF = galois_field.GaloisField(p)
        GPR = polynomial_ring.PolynomialRing(GF)
        primitive_poly = GPR.gen_primitive_poly(8)
        GEF = galois_field.GaloisField(primitive_poly)
        struct = algebraic.Structure.check(GEF)

        print(f"{GEF.__name__} is", struct)
        self.assertEqual(struct, algebraic.Structure.FIELD)

        GEPR = polynomial_ring.PolynomialRing(GEF)
        struct = algebraic.Structure.check(GEPR)

        print(f"{GEPR.__name__} is", struct)
        self.assertEqual(struct, algebraic.Structure.INTEGRAL_DOMAIN)

    def test_polynomial_ring(self):
        print()

        RPR = polynomial_ring.PolynomialRing(int)
        struct = algebraic.Structure.check(RPR)

        print(f"{RPR.__name__} is", struct)
        self.assertEqual(struct, algebraic.Structure.INTEGRAL_DOMAIN)

    def test_bits_galois_field(self):
        print()

        GEF = bits_galois_field.BitsGaloisField
        struct = algebraic.Structure.check(GEF)

        print(f"{GEF.__name__} is", struct)
        self.assertEqual(struct, algebraic.Structure.FIELD)

    def test_matrix_ring(self):
        print()

        MR = matrix.MatrixRing
        struct = algebraic.Structure.check(MR)

        print(f"{MR.__name__} is", struct)
        self.assertEqual(struct, algebraic.Structure.RING)

    def test_matrix_multi_group(self):
        print()

        MMG = matrix.MatrixMultiGroup
        struct = algebraic.Structure.check(MMG)

        print(f"{MMG.__name__} is", struct)
        self.assertEqual(struct, algebraic.Structure.GROUP)
