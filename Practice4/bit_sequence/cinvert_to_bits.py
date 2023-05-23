import binascii


def convert_to_bits(input_value):
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