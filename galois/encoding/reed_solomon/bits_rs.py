import bits_galois_field
import polynomial_ring
from encoding.reed_solomon import rs

# rs_galois_field.RS_GaloisField
bits_GEF = bits_galois_field.BitsGaloisField

# PolynomialRing[RS_GaloisField]
bits_RS = polynomial_ring.PolynomialRing(bits_GEF)

# PolynomialRing[RS_GaloisField](x)
bits_x = bits_RS([0, 1])

# GF[2^8](a)
bits_a = bits_GEF(2)


class BitsRS(rs.RS):
    def __init__(self, n, k):
        super().__init__(bits_a, n, k)

    def data_to_poly(self, data):
        return self.RS([self.GEF(byte) for byte in data[::-1]])

    def poly_to_data(self, poly):
        data = b""
        for gef in poly:
            data += gef.v.to_bytes(1, "big")
        return data[::-1]
