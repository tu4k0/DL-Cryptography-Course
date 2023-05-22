import binascii
import random


def generate_sequence():
    bits_sequence = ''.join(random.choice('01') for _ in range(20000))
    return bits_sequence


def monobit_test(bits):
    bits_1 = 0
    for i in range(len(bits)):
        if bits[i] == '1':
            bits_1 += 1
    if 9654 < bits_1 < 10346:
        status = True
    else:
        status = False

    return status


def maximum_length_of_the_series_test(bits):
    counter = 1
    series = 1
    for i in range(len(bits)):
        if i == len(bits) - 1:
            break
        if bits[i] == bits[i+1]:
            counter += 1
        elif bits[i] != bits[i+1]:
            if series < counter:
                series = counter
            counter = 1
    if series > 36:
        status = False
    else:
        status = True

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


# seq = generate_sequence()
# print(seq)
# print(convert_to_bit('mbappe'))
# print(monobit_test(seq))
# print(maximum_length_of_the_series(seq))
