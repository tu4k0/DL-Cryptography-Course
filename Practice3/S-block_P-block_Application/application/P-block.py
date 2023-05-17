import random

INPUT_DATA_SIZE = 8
OUTPUT_DATA_SIZE = 8


def p_box_calculation():
    p_box_1: list = [i for i in range(0, 8)]
    p_box_2: list = []
    p_box_3 = p_box_1.copy()
    while p_box_3:
        position = random.choice(p_box_3)
        p_box_2.append(position)
        p_box_3.remove(position)

    return p_box_1, p_box_2


def convert_to_bits(input_data):
    input_data_bin = ''
    if isinstance(input_data, int):
        input_data_bin = bin(input_data)[2:]
    elif int(input_data, 16):
        input_data_bin = bin(int(input_data, 16))[2:].zfill(INPUT_DATA_SIZE)
    elif isinstance(input_data, str):
        pass
    else:
        raise Exception('Invalid input')
    if len(input_data_bin) == 1 or len(input_data_bin) == 2:
        pass
    elif len(input_data_bin) < 8:
        input_data_bin = input_data_bin.rjust(8, '0')
    elif len(input_data_bin) > 8:
        raise Exception('Invalid input size')

    return input_data_bin


def replace_value_p_box(input_value, p_box_1, p_box_2):
    output_value_list = list('0' * OUTPUT_DATA_SIZE)
    input_value = list(input_value)
    for i in range(len(p_box_1)):
        output_value_list[p_box_2[i]] = input_value[i]

    output_value = ''.join(str(bit) for bit in output_value_list)
    return output_value


def convert_bin_to_output_hex(output_data_bin):
    return hex(int(output_data_bin, 2))[2:]


def convert_bin_to_output_int(output_data_bin):
    return int(output_data_bin, 2)


def reverse_p_box(p_box_1, p_box_2):
    reverse_p_box = list('0' * OUTPUT_DATA_SIZE)
    for i in range(len(p_box_1)):
        position = p_box_2.index(i)
        reverse_p_box[i] = p_box_1[position]

    return p_box_1, reverse_p_box


if __name__ == "__main__":
    data_type = input('Choose input data type (int/hex/bin): ')
    input_data = input('Enter data to cipher (length = 8 bits): ')
    if data_type == 'int':
        input_data = int(input_data)
    p_box_1, p_box_2 = p_box_calculation()
    input_data_binary = convert_to_bits(input_data)
    output_data_binary = replace_value_p_box(input_data_binary, p_box_1, p_box_2)
    output_data = convert_bin_to_output_hex(output_data_binary)
    print('Result of direct symmetric cryptographic P-box transformation (hex): ', output_data)
    output_data_bin = convert_to_bits(output_data)
    p_box_1, p_box_reverse = reverse_p_box(p_box_1, p_box_2)
    input_data_binary = replace_value_p_box(output_data_bin, p_box_1, p_box_reverse)
    if data_type == 'int':
        input_data = convert_bin_to_output_int(input_data_binary)
    if data_type == 'hex':
        input_data = convert_bin_to_output_hex(input_data_binary)
    print('Result of indirect symmetric cryptographic S-box transformation: ', input_data)
