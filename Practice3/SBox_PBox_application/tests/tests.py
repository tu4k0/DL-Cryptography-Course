import unittest

from Practice3.SBox_PBox_application.application.p_box import *
from Practice3.SBox_PBox_application.application.s_box import *


class Tests(unittest.TestCase):

    def test_s_box_int(self):
        input_value = 100
        s_box = s_box_generation()
        input_value_binary = convert_to_bits(input_value)
        blocks = divide_into_tetrads(input_value_binary)
        output_data_binary = search_value_s_box(blocks, s_box)
        output_data = convert_bin_to_output_hex(output_data_binary)
        output_data_bin = convert_to_bits(output_data)
        s_box_reverse = reverse_s_box(s_box)
        blocks = divide_into_tetrads(output_data_bin)
        input_data_binary = search_value_s_box(blocks, s_box_reverse)
        input_data = convert_bin_to_output_int(input_data_binary)
        self.assertEqual(input_value, input_data)

    def test_s_box_hex(self):
        input_value = 'a'
        s_box = s_box_generation()
        input_value_binary = convert_to_bits(input_value)
        blocks = divide_into_tetrads(input_value_binary)
        output_data_binary = search_value_s_box(blocks, s_box)
        output_data = convert_bin_to_output_hex(output_data_binary)
        output_data_bin = convert_to_bits(output_data)
        s_box_reverse = reverse_s_box(s_box)
        blocks = divide_into_tetrads(output_data_bin)
        input_data_binary = search_value_s_box(blocks, s_box_reverse)
        input_data = convert_bin_to_output_hex(input_data_binary)
        self.assertEqual(input_value, input_data)

    def test_s_box_size(self):
        s_box = s_box_generation()
        size = 4
        self.assertEqual(len(s_box), size)

    def test_p_box_int(self):
        input_value = 150
        p_box_1, p_box_2 = p_box_calculation()
        input_value_binary = convert_to_bits(input_value)
        output_data_binary = replace_value_p_box(input_value_binary, p_box_1, p_box_2)
        output_data = convert_bin_to_output_hex(output_data_binary)
        output_data_bin = convert_to_bits(output_data)
        p_box_1, p_box_reverse = reverse_p_box(p_box_1, p_box_2)
        input_data_binary = replace_value_p_box(output_data_bin, p_box_1, p_box_reverse)
        input_data = convert_bin_to_output_int(input_data_binary)
        self.assertEqual(input_value, input_data)

    def test_p_box_hex(self):
        input_value = 'b'
        p_box_1, p_box_2 = p_box_calculation()
        input_value_binary = convert_to_bits(input_value)
        output_data_binary = replace_value_p_box(input_value_binary, p_box_1, p_box_2)
        output_data = convert_bin_to_output_hex(output_data_binary)
        output_data_bin = convert_to_bits(output_data)
        p_box_1, p_box_reverse = reverse_p_box(p_box_1, p_box_2)
        input_data_binary = replace_value_p_box(output_data_bin, p_box_1, p_box_reverse)
        input_data = convert_bin_to_output_hex(input_data_binary)
        self.assertEqual(input_value, input_data)

    def test_p_box_formula(self):
        p_box_1, p_box_2 = p_box_calculation()
        self.assertNotEqual(p_box_1, p_box_2)

    def test_input_data_value_gt_8_bits(self):
        input_value = 300
        self.assertRaises(Exception, convert_to_bits(input_value))

    def test_input_data_value_lt_8_bits(self):
        input_value = 50
        self.assertTrue(True, convert_to_bits(input_value))

    def test_division_into_tetrads(self):
        input_data_bin = '11110000'
        blocks_size = 2
        blocks = divide_into_tetrads(input_data_bin)
        self.assertEqual(len(blocks), blocks_size)

    def test_convert_bin_to_hex(self):
        binary_data = '11110000'
        hex_data = 'f0'
        self.assertEqual(convert_bin_to_output_hex(binary_data), hex_data)

    def test_convert_bin_to_int(self):
        binary_data = '11110000'
        int_data = 240
        self.assertEqual(convert_bin_to_output_int(binary_data), int_data)


if __name__ == "__main__":
    unittest.main()
