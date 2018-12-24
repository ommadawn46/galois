import sys
import os

path = os.path.join(os.path.dirname(__file__), "../galois")
sys.path.append(path)

import unittest
import random

from galois import algebraic
from galois import matrix
from galois import galois_field
from galois import polynomial_ring
from galois import galois_extension_field
from galois import util


class TestAlgebraicStructure(unittest.TestCase):
    def test_galois_field(self):
        p = util.next_prime(random.randint(1 << 15, 1 << 16))
        GF = galois_field.GaloisField(p)
        struct = algebraic.Structure.check(GF)

        self.assertEqual(struct, algebraic.Structure.FIELD)
        print(f"\n{GF.__name__} is", struct)

    def test_real_polynomial_ring(self):
        RPR = polynomial_ring.RealPolynomialRing
        struct = algebraic.Structure.check(RPR)

        self.assertEqual(struct, algebraic.Structure.INTEGRAL_DOMAIN)
        print(f"\n{RPR.__name__} is", struct)

    def test_galois_polynomial_ring(self):
        p = util.next_prime(random.randint(1 << 15, 1 << 16))
        GF = galois_field.GaloisField(p)
        GPR = polynomial_ring.GaloisPolynomialRing(GF)
        struct = algebraic.Structure.check(GPR)

        self.assertEqual(struct, algebraic.Structure.INTEGRAL_DOMAIN)
        print(f"\n{GPR.__name__} is", struct)

    def test_galois_extension_field(self):
        p = 2
        GF = galois_field.GaloisField(p)
        GPR = polynomial_ring.GaloisPolynomialRing(GF)
        i_poly = GPR.gen_irreducible_poly(8)
        GEF = galois_extension_field.GaloisExtensionField(i_poly)
        struct = algebraic.Structure.check(GEF)

        self.assertEqual(struct, algebraic.Structure.FIELD)
        print(f"\n{GEF.__name__} is", struct)

    def test_matrix_ring(self):
        MR = matrix.MatrixRing
        struct = algebraic.Structure.check(MR)

        self.assertEqual(struct, algebraic.Structure.RING)
        print(f"\n{MR.__name__} is", struct)

    def test_matrix_multi_group(self):
        MMG = matrix.MatrixMultiGroup
        struct = algebraic.Structure.check(MMG)

        self.assertEqual(struct, algebraic.Structure.GROUP)
        print(f"\n{MMG.__name__} is", struct)
