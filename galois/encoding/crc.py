import galois_field
import polynomial_ring
import galois_extension_field
import util


p = 2
GF = galois_field.GaloisField(p)
GPR = polynomial_ring.GaloisPolynomialRing(GF)


def calc(data, width, poly_value, init_value, reflect_in, reflect_out, xor_output):
    byte_n = width // 8

    new_data = bytearray(data) + bytearray(b"\x00" * byte_n)
    init_data = init_value.to_bytes(byte_n, "big")
    for i in range(byte_n):
        new_data[i] ^= init_data[i]

    poly_data = b"\x01" + poly_value.to_bytes(byte_n, "big")
    i_poly = GPR(util.unpack_data(poly_data))
    GEF = galois_extension_field.GaloisExtensionField(i_poly)

    crc_poly = GEF(util.unpack_data(new_data, revese=reflect_in))
    crc_bits = crc_poly.v.coefs[:width]

    out = "".join(map(lambda x: str(x.v), crc_bits[::-1]))
    out = "0" * (width - len(out)) + out

    if reflect_out:
        out = out[::-1]

    return (int(out, 2) ^ xor_output).to_bytes(byte_n, "big")
