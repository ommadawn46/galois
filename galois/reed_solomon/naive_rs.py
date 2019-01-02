import util
from bits_galois_field import naive_a
from reed_solomon import rs


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
