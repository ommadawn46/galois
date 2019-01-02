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
    def algebraic_structure_test(self, A, want_struct):
        print()
        got_struct = algebraic.Structure.check(A)

        print(f"{A.__name__} is", got_struct)
        self.assertEqual(got_struct, want_struct)

    def test_galois_field(self):
        p = util.next_prime(random.randint(1 << 15, 1 << 16))
        GF = galois_field.GaloisField(p)

        self.algebraic_structure_test(GF, algebraic.Structure.FIELD)

        self.algebraic_structure_test(
            polynomial_ring.PolynomialRing(GF),
            algebraic.Structure.INTEGRAL_DOMAIN,
        )

    def test_galois_extension_field(self):
        p = 2
        GF = galois_field.GaloisField(p)
        GPR = polynomial_ring.PolynomialRing(GF)
        primitive_poly = GPR.gen_primitive_poly(8)
        GEF = galois_field.GaloisField(primitive_poly)

        self.algebraic_structure_test(GEF, algebraic.Structure.FIELD)

        self.algebraic_structure_test(
            polynomial_ring.PolynomialRing(GEF),
            algebraic.Structure.INTEGRAL_DOMAIN,
        )

    def test_polynomial_ring(self):
        self.algebraic_structure_test(
            polynomial_ring.PolynomialRing(int),
            algebraic.Structure.INTEGRAL_DOMAIN,
        )

    def test_bits_galois_field(self):
        self.algebraic_structure_test(
            bits_galois_field.BitsGaloisField, algebraic.Structure.FIELD
        )

    def test_matrix_ring(self):
        self.algebraic_structure_test(
            matrix.MatrixRing, algebraic.Structure.RING
        )

    def test_matrix_multi_group(self):
        self.algebraic_structure_test(
            matrix.MatrixMultiGroup, algebraic.Structure.GROUP
        )
