import random

INPUT_DATA_SIZE = 8
OUTPUT_DATA_SIZE = 8
BLOCK_SIZE = 4


def s_box_generation():
    s_box: list = [[None] * 4 for _ in range(4)]
    for i in range(16):
        num = random.randint(0, 15)
        while num in [item for sublist in s_box for item in sublist]:
            num = random.randint(0, 15)
        row = i // 4
        col = i % 4
        s_box[row][col] = num
    for i in range(len(s_box)):
        for j in range(len(s_box)):
            s_box[i][j] = bin(s_box[i][j])[2:].zfill(4)

    return s_box


def convert_to_bits(input_data):
    input_data_bin = ''
    if isinstance(input_data, int):
        input_data_bin = bin(input_data)[2:]
    elif int(input_data, 16):
        input_data_bin = bin(int(input_data, 16))[2:].zfill(INPUT_DATA_SIZE)
    elif int(input_data, 2):
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


def divide_into_tetrads(input_data_bin):
    blocks = [input_data_bin[0:BLOCK_SIZE], input_data_bin[BLOCK_SIZE:]]

    return blocks


def search_value_s_box(blocks, s_box):
    output_data_bin = ''
    for block in blocks:
        outer_bits = str(block)[0:2]
        inner_bits = str(block)[2:4]
        for i in range(len(s_box)):
            for j in range(len(s_box)):
                i_bin = convert_to_bits(i).rjust(2, '0')
                j_bin = convert_to_bits(j).rjust(2, '0')
                if outer_bits == i_bin and inner_bits == j_bin:
                    output_data_bin += str(s_box[i][j])

    return output_data_bin


def convert_bin_to_output_hex(output_data_bin):
    return hex(int(output_data_bin, 2))[2:]


def convert_bin_to_output_int(output_data_bin):
    return int(output_data_bin, 2)


def reverse_s_box(s_box):
    reverse_s_box: list = [[None] * 4 for _ in range(4)]
    for i in range(len(s_box)):
        for j in range(len(s_box)):
            i_bin = convert_to_bits(i).rjust(2, '0')
            j_bin = convert_to_bits(j).rjust(2, '0')
            row = int(s_box[i][j][0:2], 2)
            col = int(s_box[i][j][2:4], 2)
            reverse_s_box[row][col] = i_bin + j_bin

    return reverse_s_box


if __name__ == "__main__":
    data_type = input('Choose input data type (int/hex/bin): ')
    input_data = input('Enter data to cipher (length = 8 bits): ')
    if data_type == 'int':
        input_data = int(input_data)
    s_box = s_box_generation()
    input_data_binary = convert_to_bits(input_data)
    blocks = divide_into_tetrads(input_data_binary)
    output_data_binary = search_value_s_box(blocks, s_box)
    output_data = convert_bin_to_output_hex(output_data_binary)
    print('Result of direct symmetric cryptographic S-box transformation: ', output_data)
    output_data_bin = convert_to_bits(output_data)
    s_box_reverse = reverse_s_box(s_box)
    blocks = divide_into_tetrads(output_data_bin)
    input_data_binary = search_value_s_box(blocks, s_box_reverse)
    if data_type == 'int':
        input_data = convert_bin_to_output_int(input_data_binary)
    if data_type == 'hex':
        input_data = convert_bin_to_output_hex(input_data_binary)
    print('Result of indirect symmetric cryptographic S-box transformation: ', input_data)
