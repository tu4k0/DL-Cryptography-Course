import unittest

from Practice10.ECDSA.ECDSA import *


class Tests(unittest.TestCase):

    def test_private_key(self):
        ecdsa = ECDSA()
        ecdsa.key_generation()
        private_key = ecdsa.getPrivateKey()
        self.assertEqual(type(private_key), int)

    def test_public_key_type(self):
        ecdsa = ECDSA()
        ecdsa.key_generation()
        public_key = ecdsa.getPublicKey()
        self.assertEqual(type(public_key), ElipticCurve.EcPoint)

    def test_public_key_value(self):
        ecdsa = ECDSA()
        ecdsa.key_generation()
        public_key_x = ecdsa.getPublicKey().x
        status = all(c in string.hexdigits for c in public_key_x)
        self.assertTrue(status)

    def test_signature(self):
        ecdsa = ECDSA()
        r, s = ecdsa.sign_message('Kyrylo')
        self.assertNotEqual(r, 0.0)
        self.assertNotEqual(r, 0.0)

    def test_ECDSA(self):
        ecdsa = ECDSA()
        r, s = ecdsa.sign_message('Kyrylo')
        status = ecdsa.verify_signature('Kyrylo', r, s)
        self.assertTrue(status)

    def test_ECDSA_modified_signature(self):
        ecdsa = ECDSA()
        r, s = ecdsa.sign_message('Kyrylo')
        r = 123237
        s = 892374
        status = ecdsa.verify_signature('Kyrylo', r, s)
        self.assertFalse(status)


if __name__ == "__main__":
    unittest.main()
