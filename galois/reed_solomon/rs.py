import matrix
import polynomial_ring


def get_solutions(S):
    r = S.check_rank()
    return [S[i][r] for i in range(r)]


class RS:
    def __init__(self, a, n, k):
        self.a = a
        self.GEF = type(a)
        self.RS = polynomial_ring.PolynomialRing(self.GEF)
        self.x = self.RS([0, 1])
        self.n, self.k = n, k
        self.G = self.make_gen_poly()

    def make_gen_poly(self):
        g = self.RS.one()
        for d in range(self.n - self.k):
            g *= self.x - self.RS([self.a ** d])
        return g

    def calc_syndromes(self, poly):
        return [poly.apply(self.a ** d) for d in range(self.n - self.k + 1)]

    def check_error_exist(self, syndromes):
        for i in range(self.n - self.k):
            if syndromes[i] != self.GEF.zero():
                return True
        return False

    def make_syndrome_matrix(self, syndromes):
        t = (self.n - self.k) // 2
        m = []
        for i in range(t):
            m.append(syndromes[i : i + t + 1])
        return matrix.MatrixRing(m)

    def find_error_locations(self, error_locator_poly):
        return [
            i
            for i in range(self.n)
            if error_locator_poly.apply(self.a ** i) == self.GEF.zero()
        ]

    def make_error_matrix(self, error_locations, syndromes):
        m = []
        for i in range(len(error_locations)):
            row = []
            for j in range(len(error_locations)):
                row.append((self.a ** error_locations[j]) ** i)
            m.append(row + [syndromes[i]])
        return matrix.MatrixRing(m)

    def calc_error_poly(self, C):
        E = self.RS.zero()

        syndromes = self.calc_syndromes(C)
        if not self.check_error_exist(syndromes):
            return E
        S = self.make_syndrome_matrix(syndromes)

        error_locators = get_solutions(S.gaussian_elimination())
        error_locator_poly = self.RS(error_locators + [self.GEF.one()])
        error_locations = self.find_error_locations(error_locator_poly)

        error_matrix = self.make_error_matrix(error_locations, syndromes)
        errors = get_solutions(error_matrix.gaussian_elimination())

        for i in range(len(errors)):
            E += self.RS([errors[i]]) * self.x ** error_locations[i]

        return E

    def data_to_poly(self, data):
        raise Exception("not implemented")

    def poly_to_data(self, poly):
        raise Exception("not implemented")

    def encode_poly(self, I):
        if I.degree > self.k:
            raise Exception("too large information polynomial")
        shifted_I = I * self.x ** (self.n - self.k)
        P = shifted_I % self.G
        C = shifted_I + P
        return C

    def decode_poly(self, C):
        if C.degree > self.n + self.k:
            raise Exception("too large code polynomial")
        E = self.calc_error_poly(C)
        return self.RS((C + E)[self.n - self.k :])

    def encode(self, data):
        I = self.data_to_poly(data)
        C = self.encode_poly(I)
        return self.poly_to_data(C)

    def decode(self, data):
        C = self.data_to_poly(data)
        I = self.decode_poly(C)
        return self.poly_to_data(I)
