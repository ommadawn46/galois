import unittest

import pathmagic

with pathmagic.context():
    import elgamal


class TestEllipticCurveElGamal(unittest.TestCase):
    def test_elliptic_curve_elgamal(self):
        print()

        x, P = elgamal.gen_key_pair()
        print(f"x = {x}")
        print(f"P = {P}")

        message = b"This is a test message."
        print(f"m = {message}")
        print()

        c1, c2 = elgamal.encrypt(message, P)
        print(f"elgamal.encrypt(m, P) = (c1, c2)")
        print(f"c1 = {c1}")
        print(f"c2 = {c2}")

        decrypted = elgamal.decrypt(c1, c2, x)
        print(f"elgamal.decrypt(c1, c2, x) = {decrypted}")
        self.assertEqual(message, decrypted)
        print()

        c1_, c2_ = elgamal.encrypt(message, P)
        print(f"elgamal.encrypt(m, P) = (c1_, c2_)")
        print(f"c1_ = {c1_}")
        print(f"c2_ = {c2_}")

        decrypted_ = elgamal.decrypt(c1_, c2_, x)
        print(f"elgamal.decrypt(c1_, c2_, x) = {decrypted_}")
        self.assertEqual(message, decrypted_)
        print()

        # Different ciphertexts are generated from the same message
        self.assertNotEqual(c1, c1_)
        self.assertNotEqual(c2, c2_)
        print(f"(c1, c2) != (c1_, c2_)")
