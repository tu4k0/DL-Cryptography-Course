import binascii
import random


def generate_sequence():
    bits_sequence = ''.join(random.choice('01') for _ in range(20000))
    return bits_sequence


def monobit_test(bits):
    bits_1 = bits.count('1')
    if 9654 < bits_1 < 10346:
        status = True
    else:
        status = False

    return status

def convert_to_bit(input_value):
    input_data_bin = ''
    if isinstance(input_value, int):
        input_data_bin = bin(input_value)[2:]
    elif isinstance(input_value, str):
        try:
            int(input_value, 16)
            input_data_bin = bin(int(input_value, 16))[2:]
        except ValueError:
            input_data_hex = binascii.hexlify(input_value.encode())
            input_data_bin = bin(int(input_data_hex, 16))[2:].zfill(8 * ((len(input_data_hex) + 1) // 2))

    return input_data_bin


seq = generate_sequence()
print(len(seq))
print(convert_to_bit('mbappe'))
print(monobit_test('111110010101010011111000000'))
