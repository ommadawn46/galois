import os
import random
import sys
import unittest

path = os.path.join(os.path.dirname(__file__), "../galois")
sys.path.append(path)

import algebraic
import galois_field
import matrix
import polynomial_ring
import util


class TestAlgebraicStructure(unittest.TestCase):
    def test_galois_field(self):
        print()

        p = util.next_prime(random.randint(1 << 15, 1 << 16))
        GF = galois_field.GaloisField(p)
        struct = algebraic.Structure.check(GF)

        self.assertEqual(struct, algebraic.Structure.FIELD)
        print(f"{GF.__name__} is", struct)

        GPR = polynomial_ring.PolynomialRing(GF)
        struct = algebraic.Structure.check(GPR)

        self.assertEqual(struct, algebraic.Structure.INTEGRAL_DOMAIN)
        print(f"{GPR.__name__} is", struct)

    def test_galois_extension_field(self):
        print()

        p = 2
        GF = galois_field.GaloisField(p)
        GPR = polynomial_ring.PolynomialRing(GF)
        primitive_poly = GPR.gen_primitive_poly(8)
        GEF = galois_field.GaloisField(primitive_poly)
        struct = algebraic.Structure.check(GEF)

        self.assertEqual(struct, algebraic.Structure.FIELD)
        print(f"{GEF.__name__} is", struct)

        GEPR = polynomial_ring.PolynomialRing(GEF)
        struct = algebraic.Structure.check(GEPR)

        self.assertEqual(struct, algebraic.Structure.INTEGRAL_DOMAIN)
        print(f"{GEPR.__name__} is", struct)

    def test_polynomial_ring(self):
        print()

        RPR = polynomial_ring.PolynomialRing(int)
        struct = algebraic.Structure.check(RPR)

        self.assertEqual(struct, algebraic.Structure.INTEGRAL_DOMAIN)
        print(f"{RPR.__name__} is", struct)

    def test_matrix_ring(self):
        print()

        MR = matrix.MatrixRing
        struct = algebraic.Structure.check(MR)

        self.assertEqual(struct, algebraic.Structure.RING)
        print(f"{MR.__name__} is", struct)

    def test_matrix_multi_group(self):
        print()

        MMG = matrix.MatrixMultiGroup
        struct = algebraic.Structure.check(MMG)

        self.assertEqual(struct, algebraic.Structure.GROUP)
        print(f"{MMG.__name__} is", struct)
