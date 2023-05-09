import unittest

from large_numbers_lib import UintArray


class Tests(unittest.TestCase):

    uint_array = UintArray()

    def test_getter(self):
        self.uint_array.set_number_hex(36975474653157054774828021269746402683982340877533073654506438589893109550756)
        self.assertEqual(self.uint_array.get_number_hex(),
                         '0x51bf608414ad5726a3c1bec098f77b1b54ffb2787f8d528a74c1d7fde6470ea4')


if __name__ == "__main__":
    unittest.main()
