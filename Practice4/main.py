from Practice4.key_standard.FIPS140_3 import monobit_test, maximum_length_of_the_series_test, pokker_test, series_length_test
from Practice4.bit_sequence.generate_bit_sequence import generate_bit_sequence


if __name__ == '__main__':
    seq = generate_bit_sequence()
    test_1 = monobit_test(seq)
    test_2 = maximum_length_of_the_series_test(seq)
    test_3 = pokker_test(seq)
    test_4 = series_length_test(seq)
    if test_1 and test_2 and test_3 and test_4 == True:
        print('The 20,000-bit sequence is sufficiently random')
    else:
        print('The bit sequence is rejected')
