from bits_galois_field import bits_a
from reed_solomon import rs


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
