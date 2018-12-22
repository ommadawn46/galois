import unittest
import random

from algebraic_structure import AlgebraicStructure

import prime_number
import matrix
import galois_field
import polynomial_ring
import galois_extension_field


class TestAlgebraicStructure(unittest.TestCase):
    def test_galois_field(self):
        p = prime_number.next_prime(random.randint(1 << 15, 1 << 16))
        GF = galois_field.GaloisField(p)
        struct = AlgebraicStructure.check(GF)

        self.assertEqual(struct, AlgebraicStructure.FIELD)
        print(f"\n{GF.__name__} is", struct)

    def test_real_polynomial_ring(self):
        RPR = polynomial_ring.RealPolynomialRing
        struct = AlgebraicStructure.check(RPR)

        self.assertEqual(struct, AlgebraicStructure.INTEGRAL_DOMAIN)
        print(f"\n{RPR.__name__} is", struct)

    def test_galois_polynomial_ring(self):
        p = prime_number.next_prime(random.randint(1 << 15, 1 << 16))
        GF = galois_field.GaloisField(p)
        GPR = polynomial_ring.GaloisPolynomialRing(GF)
        struct = AlgebraicStructure.check(GPR)

        self.assertEqual(struct, AlgebraicStructure.INTEGRAL_DOMAIN)
        print(f"\n{GPR.__name__} is", struct)

    def test_galois_extension_field(self):
        p = 2
        GF = galois_field.GaloisField(p)
        GPR = polynomial_ring.GaloisPolynomialRing(GF)
        i_poly = polynomial_ring.generate_irreducible_polynomial(GPR, 8)
        GEF = galois_extension_field.GaloisExtensionField(i_poly)
        struct = AlgebraicStructure.check(GEF)

        self.assertEqual(struct, AlgebraicStructure.FIELD)
        print(f"\n{GEF.__name__} is", struct)

    def test_matrix_ring(self):
        MR = matrix.MatrixRing
        struct = AlgebraicStructure.check(MR)

        self.assertEqual(struct, AlgebraicStructure.RING)
        print(f"\n{MR.__name__} is", struct)

    def test_matrix_multi_group(self):
        MMG = matrix.MatrixMultiGroup
        struct = AlgebraicStructure.check(MMG)

        self.assertEqual(struct, AlgebraicStructure.GROUP)
        print(f"\n{MMG.__name__} is", struct)
