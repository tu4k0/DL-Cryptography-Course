import struct


class BigInteger:
    number_hex: str
    bin_array: list

    def __init__(self):
        self.uint_array = []
        self.number = 0
        self.number_bin_array = []

    def set_hex(self, _number_hex):
        self.number_hex = _number_hex

    def get_hex(self):
        return self.number_hex

    def convert_from_hex_to_bin(self, number):
        number_bin = bin(int(number, 16))[2:]
        index_start = 0
        index_stop = 64
        if len(number_bin) < 64:
            self.uint_array.append(number_bin.zfill(64))
        else:
            for i in range(1, len(number_bin) // 64 + 1):
                self.uint_array.append(number_bin[index_start:index_stop])
                index_start += 64
                index_stop += 64
            if len(number_bin) % 64 != 0:
                self.uint_array.append(number_bin[-(len(number_bin) % 64):])

        return self.uint_array

    def convert_from_bin_to_hex(self):
        result = ''
        for binary in self.uint_array:
            result += str(binary)

        result = hex(int(result, 2))[2:]

        return result

    def break_into_chunks(self, number_bin):
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

    def compare_numbers_bin(self, number_1, number_2):
        if len(number_1) < len(number_2):
            number_1 = number_1.zfill(len(number_2))
        elif len(number_2) < len(number_1):
            number_2 = number_2.zfill(len(number_1))

        return number_1, number_2

    def XOR(self, number_1, number_2):
        number_1 = bin(int(number_1, 16))[2:]
        number_2 = bin(int(number_2, 16))[2:]
        number_1, number_2 = self.compare_numbers_bin(number_1, number_2)
        number_1 = self.break_into_chunks(number_1)
        number_2 = self.break_into_chunks(number_2)
        for i in range(0, len(number_1)):
            binary = ''
            for j in range(0, len(number_1[i])):
                if number_1[i][j] == '1' and number_2[i][j] == '1':
                    binary += '0'
                elif number_1[i][j] == '1' or number_2[i][j] == '1':
                    binary += '1'
                else:
                    binary += '0'
            self.uint_array.append(binary)
        self.number_hex = self.convert_from_bin_to_hex()

    def INV(self, number_1):
        number_1 = bin(int(number_1, 16))[2:]
        number_1 = self.break_into_chunks(number_1)
        for i in range(0, len(number_1)):
            binary = ''
            for j in range(0, len(number_1[i])):
                if number_1[i][j] == '1':
                    binary += '0'
                else:
                    binary += '1'
            self.uint_array.append(binary)
        self.number_hex = self.convert_from_bin_to_hex()

    def OR(self, number_1, number_2):
        number_1 = bin(int(number_1, 16))[2:]
        number_2 = bin(int(number_2, 16))[2:]
        number_1, number_2 = self.compare_numbers_bin(number_1, number_2)
        number_1 = self.break_into_chunks(number_1)
        number_2 = self.break_into_chunks(number_2)
        for i in range(0, len(number_1)):
            binary = ''
            for j in range(0, len(number_1[i])):
                if number_1[i][j] == '0' and number_2[i][j] == '0':
                    binary += '0'
                else:
                    binary += '1'
            self.uint_array.append(binary)
        self.number_hex = self.convert_from_bin_to_hex()

    def AND(self, number_1, number_2):
        number_1 = bin(int(number_1, 16))[2:]
        number_2 = bin(int(number_2, 16))[2:]
        number_1, number_2 = self.compare_numbers_bin(number_1, number_2)
        number_1 = self.break_into_chunks(number_1)
        number_2 = self.break_into_chunks(number_2)
        for i in range(0, len(number_1)):
            binary = ''
            for j in range(0, len(number_1[i])):
                if number_1[i][j] == '1' and number_2[i][j] == '1':
                    binary += '1'
                else:
                    binary += '0'
            self.uint_array.append(binary)
        self.number_hex = self.convert_from_bin_to_hex()

    def shiftL(self, number_1, bits):
        number_1 = bin(int(number_1, 16))[2:]
        number_1 = self.break_into_chunks(number_1)
        for i in range(0, len(number_1)):
            if i == len(number_1)-1:
                binary = number_1[i]
                for bit in range(0, bits):
                    binary += '0'
                self.uint_array.append(binary)
            else:
                self.uint_array.append(number_1[i])
        self.number_hex = self.convert_from_bin_to_hex()

    def shiftR(self, number_1, bits):
        number_1 = bin(int(number_1, 16))[2:]
        number_1 = self.break_into_chunks(number_1)
        for i in range(0, len(number_1)):
            if i == len(number_1) - 1:
                binary = number_1[i]
                self.uint_array.append(binary[:-bits])
            else:
                self.uint_array.append(number_1[i])
        self.number_hex = self.convert_from_bin_to_hex()


a = BigInteger()
b = BigInteger()
c = BigInteger()
d = BigInteger()
e = BigInteger()
f = BigInteger()
a.set_hex('e035c6cfa42609b998b883bc1699df885cef74e2b2cc372eb8fa7e7')
b.set_hex('5072f028943e0fd5fab3273782de14b1011741bd0c5cd6ba6474330')
# c.XOR(a.number_hex, b.number_hex)
# print(c.get_hex())
# a.INV(a.number_hex)
# print(a.get_hex())
# d.OR(a.number_hex, b.number_hex)
# print(int(d.get_hex(), 16))
# e.AND(a.number_hex, b.number_hex)
# print(e.get_hex())
# f.shiftR(a.number_hex, 2)
# print(a.convert_from_hex_to_bin(a.number_hex))
# print(f.uint_array)