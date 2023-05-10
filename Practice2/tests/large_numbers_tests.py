import unittest

from Practice2.lib.large_numbers_lib import BigInteger


class Tests(unittest.TestCase):

    def test_setter(self):
        number_value = '51bf608414ad5726a3c1bec098f77b1b54ffb2787f8d528a74c1d7fde6470ea4'
        number_1 = BigInteger()
        number_1.set_hex(number_value)
        self.assertEqual(number_1.number_hex, '51bf608414ad5726a3c1bec098f77b1b54ffb2787f8d528a74c1d7fde6470ea4')

    def test_getter(self):
        number_value = '34aa714414ad7826a3c1bec098f77b1b54ffb2787f8d528a74c1d7fde6470be2'
        number_2 = BigInteger()
        number_2.set_hex(number_value)
        self.assertEqual(number_2.get_hex(), '34aa714414ad7826a3c1bec098f77b1b54ffb2787f8d528a74c1d7fde6470be2')

    def test_from_hex_to_bin(self):
        number_value = '51bf608414ad5726a3c1bec098f77b1b54ffb2787f8d528a74c1d7fde6470ea4'
        number_3 = BigInteger()
        number_3.set_hex(number_value)
        self.assertEqual(number_3.convert_from_hex_to_bin(number_3.number_hex), '0101000110111111011000001000010000010100101011010101011100100110101000111100000110111110110000001001100011110111011110110001101101010100111111111011001001111000011111111000110101010010100010100111010011000001110101111111110111100110010001110000111010100100')

    def test_from_bin_to_hex(self):
        number_4 = BigInteger()
        number_4.uint_array = ['0101000110111111011000001000010000010100101011010101011100100110101000111100000110111110110000001001100011110111011110110001101101010100111111111011001001111000011111111000110101010010100010100111010011000001110101111111110111100110010001110000111010100100']
        self.assertEqual(number_4.convert_from_bin_to_hex(), '51bf608414ad5726a3c1bec098f77b1b54ffb2787f8d528a74c1d7fde6470ea4')

    def test_XOR(self):
        numberA = BigInteger()
        numberB = BigInteger()
        numberC = BigInteger()
        numberA.set_hex('51bf608414ad5726a3c1bec098f77b1b54ffb2787f8d528a74c1d7fde6470ea4')
        numberB.set_hex('403db8ad88a3932a0b7e8189aed9eeffb8121dfac05c3512fdb396dd73f6331c')
        numberC.XOR(numberA.number_hex, numberB.number_hex)
        self.assertEqual(numberC.number_hex, '1182d8299c0ec40ca8bf3f49362e95e4ecedaf82bfd167988972412095b13db8')

    def test_INV(self):
        numberA = BigInteger()
        numberA.set_hex('e035c6cfa42609b998b883bc1699df885cef74e2b2cc372eb8fa7e7')
        numberA.INV(numberA.number_hex)
        self.assertEqual(numberA.number_hex, '1fca39305bd9f64667477c43e9662077a3108b1d4d33c8d14705818')

    def test_AND(self):
        numberA = BigInteger()
        numberB = BigInteger()
        numberC = BigInteger()
        numberA.set_hex('e035c6cfa42609b998b883bc1699df885cef74e2b2cc372eb8fa7e7')
        numberB.set_hex('5072f028943e0fd5fab3273782de14b1011741bd0c5cd6ba6474330')
        numberC.AND(numberA.number_hex, numberB.number_hex)
        self.assertEqual(numberC.number_hex, '4030c0088426099198b0033402981480000740a0004c162a2070320')

    def test_shiftL(self):
        numberA = BigInteger()
        numberA.set_hex('e035c6cfa42609b998b883bc1699df885cef74e2b2cc372eb8fa7e7')
        numberA.shiftL(numberA.number_hex, 2)
        self.assertEqual(numberA.number_hex, '380d71b3e909826e662e20ef05a677e2173bdd38acb30dcbae3e9f9c')

    def test_ADD(self):
        numberA = BigInteger()
        numberB = BigInteger()
        numberC = BigInteger()
        numberA.set_hex('36f028580bb02cc8272a9a020f4200e346e276ae664e45ee80745574e2f5ab80')
        numberB.set_hex('70983d692f648185febe6d6fa607630ae68649f7e6fc45b94680096c06e4fadb')
        numberC.ADD(numberA.number_hex, numberB.number_hex)
        self.assertEqual(numberC.number_hex, 'a78865c13b14ae4e25e90771b54963ee2d68c0a64d4a8ba7c6f45ee0e9daa65b')

    def test_SUB(self):
        numberA = BigInteger()
        numberB = BigInteger()
        numberC = BigInteger()
        numberA.set_hex('33ced2c76b26cae94e162c4c0d2c0ff7c13094b0185a3c122e732d5ba77efebc')
        numberB.set_hex('22e962951cb6cd2ce279ab0e2095825c141d48ef3ca9dabf253e38760b57fe03')
        numberC.SUB(numberA.number_hex, numberB.number_hex)
        self.assertEqual(numberC.number_hex, '10e570324e6ffdbc6b9c813dec968d9bad134bc0dbb061530934f4e59c2700b9')

    def test_MOD(self):
        numberA = BigInteger()
        numberB = BigInteger()
        numberC = BigInteger()
        numberA.set_hex('e035c6cfa42609b998b883bc1699df885cef74e2b2cc372eb8fa7e7')
        numberB.set_hex('5072f028943e0fd5fab3273782de14b1011741bd0c5cd6ba6474330')
        numberC.MOD(numberA.number_hex, numberB.number_hex)
        self.assertEqual(numberC.number_hex, '4030c0088426099198b0033402981480000740a0004c162a2070327')


if __name__ == "__main__":
    unittest.main()
