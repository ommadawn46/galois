import galois_field
import matrix
import polynomial_ring
import util

p = 2

# GaloisField[2]
GF = galois_field.GaloisField(p)

# PolynomialRing[GaloisField[2]]
GPR = polynomial_ring.PolynomialRing(GF)

# PolynomialRing[GaloisField[2]](a^8 + a^4 + a^3 + a^2 + 1)
primitive_poly = GPR.gen_primitive_poly(8)

# GaloisField[a^8 + a^4 + a^3 + a^2 + 1]
GEF = galois_field.GaloisField(primitive_poly)

# PolynomialRing[GaloisField[a^8 + a^4 + a^3 + a^2 + 1]]
RS = polynomial_ring.PolynomialRing(GEF)

# PolynomialRing[GaloisField[a^8 + a^4 + a^3 + a^2 + 1]](x)
x = RS([0, 1])

# GaloisField[a^8 + a^4 + a^3 + a^2 + 1](a)
a = GEF([0, 1])


def data_to_poly(data):
    bin_list = util.unpack_data(data)
    return RS([GEF(byte) for byte in util.bin_to_byte(bin_list)])


def poly_to_data(poly):
    data = b""
    for gef in poly:
        data += util.pack_bin_list([gf.v for gf in gef.v])
    return data[::-1]


def make_gen_poly(t):
    g = RS.one()
    for d in range(t):
        g *= x - RS([a ** d])
    return g


def calc_syndromes(poly, t):
    return [poly.apply(a ** d) for d in range(t + 1)]


def make_syndrome_matrix(syndromes, k):
    m = []
    for i in range(k):
        m.append(syndromes[i : i + k + 1])
    return matrix.MatrixRing(m)


def get_solutions(S):
    r = S.check_rank()
    return [S[i][r] for i in range(r)]


def find_error_locations(error_locator_poly, n):
    return [
        i for i in range(n) if error_locator_poly.apply(a ** i) == GEF.zero()
    ]


def make_error_matrix(error_locations, syndromes):
    m = []
    for i in range(len(error_locations)):
        row = []
        for j in range(len(error_locations)):
            row.append((a ** error_locations[j]) ** i)
        m.append(row + [syndromes[i]])
    return matrix.MatrixRing(m)


def calc_error_poly(C, n, k):
    syndromes = calc_syndromes(C, n - k)
    S = make_syndrome_matrix(syndromes, (n - k) // 2)

    error_locators = get_solutions(S.gaussian_elimination())
    error_locator_poly = RS(error_locators + [GEF.one()])
    error_locations = find_error_locations(error_locator_poly, n)

    error_matrix = make_error_matrix(error_locations, syndromes)
    errors = get_solutions(error_matrix.gaussian_elimination())

    E = RS.zero()
    for i in range(len(errors)):
        E += RS([errors[i]]) * x ** error_locations[i]

    return E


def encode(I, n, k):
    G = make_gen_poly(n - k)
    shifted_I = I * x ** (n - k)
    P = shifted_I % G
    C = shifted_I + P
    return C


def decode(C, n, k):
    E = calc_error_poly(C, n, k)
    return RS((C + E)[-k:])
