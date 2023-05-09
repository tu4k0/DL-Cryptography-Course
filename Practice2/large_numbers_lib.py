import struct


class UintArray:
    uint_array: list

    def __init__(self):
        self.uint_array = []

    def set_number_dec(self, _number):
        self.uint_array.append(_number)

    def get_number_dec(self):
        return int(self.uint_array[-1])

    def set_number_hex(self, _number):
        self.uint_array.append(hex(_number))

    def get_number_hex(self):
        return str(self.uint_array[-1])

    def set_number_bytes(self, _number):
        self.uint_array.append(struct.pack("I", _number))

    def get_number_bytes(self):
        return bytes(self.uint_array[-1])

number_hex = str(0x51bf608414ad5726a3c1bec098f77b1b54ffb2787f8d528a74c1d7fde6470ea4)

a = UintArray()
a.set_number_hex(36975474653157054774828021269746402683982340877533073654506438589893109550756)
print(a.get_number_hex())