import unittest

from Practice9.ECDH.ECDH import *


class Tests(unittest.TestCase):

    def test_private_key(self):
        person_1 = Person()
        person_1.private_key = generate_private_key().private_numbers().private_value
        self.assertTrue(type(person_1), int)

    def test_public_key(self):
        person_1 = Person()
        person_1.private_key = generate_private_key()
        person_1.public_key = compute_public_key(person_1.private_key)
        ec = ElipticCurve()
        ec.EcPoint.x = person_1.public_key.x
        ec.EcPoint.y = person_1.public_key.y
        self.assertTrue(ec.is_on_curve(), True)

    def test_public_key_exchanging(self):
        person_1 = Person()
        person_1.private_key = generate_private_key()
        person_1.public_key = compute_public_key(person_1.private_key)
        person_1.public_key_initial = person_1.public_key
        person_2 = Person()
        person_2.private_key = generate_private_key()
        person_2.public_key = compute_public_key(person_2.private_key)
        person_2.public_key_initial = person_2.public_key
        exchange_public_keys(person_1, person_2)
        self.assertNotEqual(person_1.public_key_initial, person_1.public_key)
        self.assertNotEqual(person_2.public_key_initial, person_2.public_key)

    def test_ECDH(self):
        person_1 = Person()
        person_2 = Person()
        person_1.private_key = generate_private_key()
        person_2.private_key = generate_private_key()
        person_1.public_key = compute_public_key(person_1.private_key)
        person_2.public_key = compute_public_key(person_2.private_key)
        exchange_public_keys(person_1, person_2)
        ec = ElipticCurve()
        c = ec.scalar_EC_point(person_1.private_key.private_numbers().private_value, person_1)
        d = ec.scalar_EC_point(person_2.private_key.private_numbers().private_value, person_2)
        self.assertEqual(c.x, d.x)


if __name__ == "__main__":
    unittest.main()
