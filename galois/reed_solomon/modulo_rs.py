import galois_field
from reed_solomon import rs

# encode only ASCII characters
p = 101

# GaloisField[101]
modulo_GF = galois_field.GaloisField(p)

# GaloisField[101](2)
modulo_a = modulo_GF(2)


class ModuloRS(rs.RS):
    def __init__(self, n, k):
        super().__init__(modulo_a, n, k)

    def data_to_poly(self, data):
        coefs = []
        for byte in data[::-1]:
            char = byte - 0x20
            if char > p:
                raise
            coefs.append(self.GEF(char % p))
        return self.RS(coefs)

    def poly_to_data(self, poly):
        data = b""
        for gef in poly:
            byte = gef.v + 0x20
            data += byte.to_bytes(1, "big")
        return data[::-1]
