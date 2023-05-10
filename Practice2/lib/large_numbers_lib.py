from math import log2


class BigInteger:
    number_hex: str
    uint_array: list

    def __init__(self):
        self.uint_array = []
        self.number_hex = ''

    def set_hex(self, _number_hex):
        self.number_hex = _number_hex

    def get_hex(self) -> str:
        return self.number_hex

    def convert_from_hex_to_bin(self, number_hex) -> str:
        return bin(int(number_hex, 16))[2:].zfill(int(len(number_hex) * log2(16)))

    def convert_from_bin_to_hex(self) -> str:
        result = ''
        for bin_cell in self.uint_array:
            result += str(bin_cell)

        result = hex(int(result, 2))[2:]

        return result

    def break_into_chunks(self, number_bin) -> list:
        number_bin_array = []
        index_start = 0
        index_stop = 64
        if len(number_bin) < 64:
            number_bin_array.append(number_bin.zfill(64))
        else:
            for i in range(1, len(number_bin) // 64 + 1):
                number_bin_array.append(number_bin[index_start:index_stop])
                index_start += 64
                index_stop += 64
            if len(number_bin) % 64 != 0:
                number_bin_array.append(number_bin[-(len(number_bin) % 64):])

        return number_bin_array

    def compare_numbers_bin(self, number_bin_1, number_bin_2):
        if len(number_bin_1) < len(number_bin_2):
            number_bin_1 = number_bin_1.zfill(len(number_bin_2))
        elif len(number_bin_2) < len(number_bin_1):
            number_bin_2 = number_bin_2.zfill(len(number_bin_1))

        return number_bin_1, number_bin_2

    def XOR(self, number_hex_1, number_hex_2):
        number_bin_1 = self.convert_from_hex_to_bin(number_hex_1)
        number_bin_2 = self.convert_from_hex_to_bin(number_hex_2)
        number_bin_1, number_bin_2 = self.compare_numbers_bin(number_bin_1, number_bin_2)
        number_bin_1 = self.break_into_chunks(number_bin_1)
        number_bin_2 = self.break_into_chunks(number_bin_2)
        for i in range(0, len(number_bin_1)):
            binary = ''
            for j in range(0, len(number_bin_1[i])):
                if number_bin_1[i][j] == '1' and number_bin_2[i][j] == '1':
                    binary += '0'
                elif number_bin_1[i][j] == '1' or number_bin_2[i][j] == '1':
                    binary += '1'
                else:
                    binary += '0'
            self.uint_array.append(binary)
        self.number_hex = self.convert_from_bin_to_hex()

    def INV(self, number):
        number = self.convert_from_hex_to_bin(number)
        for i in range(0, len(number)):
            binary = ''
            if number[i] == '1':
                binary += '0'
            elif number[i] == '0':
                binary += '1'
            self.uint_array.append(binary)
        self.number_hex = self.convert_from_bin_to_hex()

    def OR(self, number_hex_1, number_hex_2):
        number_bin_1 = self.convert_from_hex_to_bin(number_hex_1)
        number_bin_2 = self.convert_from_hex_to_bin(number_hex_2)
        number_bin_1, number_bin_2 = self.compare_numbers_bin(number_bin_1, number_bin_2)
        number_bin_1 = self.break_into_chunks(number_bin_1)
        number_bin_2 = self.break_into_chunks(number_bin_2)
        for i in range(0, len(number_bin_1)):
            binary = ''
            for j in range(0, len(number_bin_1[i])):
                if number_bin_1[i][j] == '0' and number_bin_2[i][j] == '0':
                    binary += '0'
                else:
                    binary += '1'
            self.uint_array.append(binary)
        self.number_hex = self.convert_from_bin_to_hex()

    def AND(self, number_hex_1, number_hex_2):
        number_bin_1 = self.convert_from_hex_to_bin(number_hex_1)
        number_bin_2 = self.convert_from_hex_to_bin(number_hex_2)
        number_bin_1, number_bin_2 = self.compare_numbers_bin(number_bin_1, number_bin_2)
        number_bin_1 = self.break_into_chunks(number_bin_1)
        number_bin_2 = self.break_into_chunks(number_bin_2)
        for i in range(0, len(number_bin_1)):
            binary = ''
            for j in range(0, len(number_bin_1[i])):
                if number_bin_1[i][j] == '1' and number_bin_2[i][j] == '1':
                    binary += '1'
                else:
                    binary += '0'
            self.uint_array.append(binary)
        self.number_hex = self.convert_from_bin_to_hex()

    def shiftL(self, number_hex, bits):
        number_bin = self.convert_from_hex_to_bin(number_hex)
        binary = number_bin
        for bit in range(0, bits):
            binary += '0'
        self.uint_array.append(binary)
        self.number_hex = self.convert_from_bin_to_hex()

    def shiftR(self, number_hex, bits):
        number_bin = self.convert_from_hex_to_bin(number_hex)
        binary = number_bin
        self.uint_array.append(binary[:-bits])
        self.number_hex = self.convert_from_bin_to_hex()

    def ADD(self, number_hex_1, number_hex_2):
        number_bin_1 = self.convert_from_hex_to_bin(number_hex_1)
        number_bin_2 = self.convert_from_hex_to_bin(number_hex_2)
        number_bin_1, number_bin_2 = self.compare_numbers_bin(number_bin_1, number_bin_2)
        number_1 = int(number_bin_1, 2)
        number_2 = int(number_bin_2, 2)
        while number_2 != 0:
            carry = number_1 & number_2
            number_1 = number_1 ^ number_2
            number_2 = carry << 1
        self.uint_array.append(str(bin(number_1))[2:])
        self.number_hex = self.convert_from_bin_to_hex()

    def SUB(self, number_hex_1, number_hex_2):
        number_bin_1 = self.convert_from_hex_to_bin(number_hex_1)
        number_bin_2 = self.convert_from_hex_to_bin(number_hex_2)
        number_bin_1, number_bin_2 = self.compare_numbers_bin(number_bin_1, number_bin_2)
        number_1 = int(number_bin_1, 2)
        number_2 = int(number_bin_2, 2)
        while number_2 != 0:
            borrow = (~number_1) & number_2
            number_1 = number_1 ^ number_2
            number_2 = borrow << 1
        self.uint_array.append(str(bin(number_1))[2:])
        self.number_hex = self.convert_from_bin_to_hex()

    def MOD(self, number_hex_1, number_hex_2):
        number_bin_1 = self.convert_from_hex_to_bin(number_hex_1)
        number_bin_2 = self.convert_from_hex_to_bin(number_hex_2)
        number_bin_1, number_bin_2 = self.compare_numbers_bin(number_bin_1, number_bin_2)
        number_1 = int(number_bin_1, 2)
        number_2 = int(number_bin_2, 2)
        number_1 = number_1 & number_2 - 1
        self.uint_array.append(str(bin(number_1))[2:])
        self.number_hex = self.convert_from_bin_to_hex()
