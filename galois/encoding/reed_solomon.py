import random

import algebraic
import matrix
import galois_field
import polynomial_ring
import galois_extension_field
import util

p = 2

# GaloisField[2]
GF = galois_field.GaloisField(p)

# GaloisPolynomialRing[2]
GPR = polynomial_ring.GaloisPolynomialRing(GF)

# GaloisPolynomialRing[2](a^8 + a^4 + a^3 + a^2 + 1)
primitive_poly = GPR([1, 0, 1, 1, 1, 0, 0, 0, 1])

# GaloisExtensionField[a^8 + a^4 + a^3 + a^2 + 1]
GEF = galois_extension_field.GaloisExtensionField(primitive_poly)

# GaloisPolynomialRing[a^8 + a^4 + a^3 + a^2 + 1]
RS = polynomial_ring.GaloisPolynomialRing(GEF)
RS.VARCHAR = "x"

# GaloisPolynomialRing[a^8 + a^4 + a^3 + a^2 + 1](x)
x = RS([GEF([0]), GEF([1])])

# GaloisExtensionField[a^8 + a^4 + a^3 + a^2 + 1](a)
a = GEF([0, 1])


def data_to_rs_poly(data):
    bin_list = util.unpack_data(data)
    return RS([GEF(byte) for byte in util.bin_to_byte(bin_list)])


def rs_poly_to_data(poly):
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
    return m


def gaussian_elimination(m):
    m = m[:]
    for i in range(len(m)):
        c1, j = m[i][i], i + 1
        while c1 == c1.zero() and j < len(m):
            # pivot
            m[i], m[j] = m[j], m[i]
            c1, j = m[i][i], j + 1
        if c1 == c1.zero():
            continue

        m[i] = [m[i][j] / c1 for j in range(len(m[i]))]
        for j in range(len(m)):
            if i == j:
                continue
            c2 = m[j][i]
            m[j] = [m[j][k] - m[i][k] * c2 for k in range(len(m[j]))]
    return m


def check_rank(S):
    for i in range(len(S)):
        if S[i][i] != S[i][i].one():
            return i
    return len(S)


def get_solutions(S):
    r = check_rank(S)
    return [S[i][r] for i in range(r)]


def find_error_locations(error_locator_poly, n):
    return [i for i in range(n) if error_locator_poly.apply(a ** i) == GEF.zero()]


def make_error_matrix(error_locations, syndromes):
    m = []
    for i in range(len(error_locations)):
        row = []
        for j in range(len(error_locations)):
            row.append((a ** error_locations[j]) ** i)
        m.append(row + [syndromes[i]])
    return m


def calc_error_poly(C, n, k):
    syndromes = calc_syndromes(C, n - k)
    S = make_syndrome_matrix(syndromes, (n - k) // 2)
    S = gaussian_elimination(S)

    error_locators = get_solutions(S)
    error_locator_poly = RS(error_locators + [GEF.one()])
    error_locations = find_error_locations(error_locator_poly, n)

    error_matrix = make_error_matrix(error_locations, syndromes)
    error_matrix = gaussian_elimination(error_matrix)
    errors = get_solutions(error_matrix)

    E = RS.zero()
    for i in range(len(errors)):
        E += RS([errors[i]]) * x ** error_locations[i]

    return E


def encode(I, n, k):
    G = make_gen_poly(n - k)
    I_pad = I * x ** (n - k)
    P = I_pad % G
    C = I_pad + P
    return C


def decode(C, n, k):
    E = calc_error_poly(C, n, k)
    return RS((C + E).coefs[-k:])
