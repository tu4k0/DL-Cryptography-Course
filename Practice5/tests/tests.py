import unittest

from Practice5.hashing_algorithms.SHA1_own import SHA1_own
from Practice5.hashing_algorithms.SHA1_lib import SHA1_lib


class Tests(unittest.TestCase):

    def test_SHA1_hash_match_own_with_lib(self):
        input_text = 'Distributed Lab'
        hash_1 = SHA1_own(input_text)
        hash_2 = SHA1_lib(input_text)
        self.assertEqual(hash_1, hash_2)


if __name__ == "__main__":
    unittest.main()
