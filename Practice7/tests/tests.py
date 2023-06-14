import unittest

from Practice7.digital_signature import Elgamal_signature
from Practice7.encryption import Elgamal_encryption


class Tests(unittest.TestCase):

    def test_Elgamal_signature(self):
        input_text = 'Kyrylo'
        p, q = Elgamal_signature.generate_random_prime_number()
        a, b = Elgamal_signature.key_generation(p, q)
        r, s, m = Elgamal_signature.sign_message(p, q, a, input_text)
        verification_status = Elgamal_signature.check_signature(p, q, b, r, s, m)
        self.assertTrue(True, verification_status)

    def test_Elgamal_signature_modified_data(self):
        input_text = 'Kyrylo'
        p, q = Elgamal_signature.generate_random_prime_number()
        a, b = Elgamal_signature.key_generation(p, q)
        r, s, m = Elgamal_signature.sign_message(p, q, a, input_text)
        r = 1
        s = 2
        verification_status = Elgamal_signature.check_signature(p, q, b, r, s, m)
        self.assertFalse(False, verification_status)

    def test_Elgamal_encryption(self):
        message = 'Kyrylo'
        blocks = Elgamal_encryption.create_blocks(message)
        p, g = Elgamal_encryption.generate_random_prime_number()
        a, b = Elgamal_encryption.key_generation(p, g)
        x, y = Elgamal_encryption.encrypt_message(blocks, p, g, b)
        m = Elgamal_encryption.decrypt_message(x, y, a, p)
        self.assertEqual(message, m)


if __name__ == "__main__":
    unittest.main()
