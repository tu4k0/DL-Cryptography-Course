import unittest

from Practice4.key_standard.FIPS140_3 import monobit_test, maximum_length_of_the_series_test, pokker_test, series_length_test
from Practice4.bit_sequence.generate_bit_sequence import generate_bit_sequence
from Practice4.bit_sequence.convert_to_bits import convert_to_bits


class Tests(unittest.TestCase):

    def test_convert_int_to_bits(self):
        input_data_int = 24052023
        input_data_bits = convert_to_bits(input_data_int)
        self.assertEqual(input_data_bits, '1011011110000000100110111')

    def test_convert_text_to_bits(self):
        input_data_text = 'Kyrylo'
        input_data_bits = convert_to_bits(input_data_text)
        self.assertEqual(input_data_bits, '010010110111100101110010011110010110110001101111')

    def test_convert_hex_to_bits(self):
        input_data_hex = 'afa'
        input_data_bits = convert_to_bits(input_data_hex)
        self.assertEqual(input_data_bits, '101011111010')

    def test_bit_sequence_length(self):
        sequence = generate_bit_sequence()
        self.assertEqual(len(sequence), 20000)

    def test_monobit(self):
        sequence = generate_bit_sequence()
        self.assertTrue(True, monobit_test(sequence))

    def test_maximum_length_of_the_series(self):
        sequence = generate_bit_sequence()
        self.assertTrue(True, maximum_length_of_the_series_test(sequence))

    def test_pokker(self):
        sequence = generate_bit_sequence()
        self.assertTrue(True, pokker_test(sequence))

    def test_series_length(self):
        sequence = generate_bit_sequence()
        self.assertTrue(True, series_length_test(sequence))


if __name__ == "__main__":
    unittest.main()
