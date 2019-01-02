import galois_field
import polynomial_ring
import util
from encoding.reed_solomon import rs

p = 2

# GaloisField[2]
GF = galois_field.GaloisField(p)

# PolynomialRing[GaloisField[2]]
GPR = polynomial_ring.PolynomialRing(GF)

# PolynomialRing[GaloisField[2]](a^8 + a^4 + a^3 + a^2 + 1)
prime_poly = GPR.gen_primitive_poly(8)

# GaloisField[a^8 + a^4 + a^3 + a^2 + 1]
naive_GEF = galois_field.GaloisField(prime_poly)

# PolynomialRing[GaloisField[a^8 + a^4 + a^3 + a^2 + 1]]
naive_RS = polynomial_ring.PolynomialRing(naive_GEF)

# PolynomialRing[GaloisField[a^8 + a^4 + a^3 + a^2 + 1]](x)
naive_x = naive_RS([0, 1])

# GaloisField[a^8 + a^4 + a^3 + a^2 + 1](a)
naive_a = naive_GEF([0, 1])


class NaiveRS(rs.RS):
    def __init__(self, n, k):
        super().__init__(naive_a, n, k)

    def data_to_poly(self, data):
        bin_list = util.unpack_data(data)
        return self.RS([self.GEF(byte) for byte in util.bin_to_byte(bin_list)])

    def poly_to_data(self, poly):
        data = b""
        for gef in poly:
            data += util.pack_bin_list([gf.v for gf in gef.v])
        return data[::-1]
