import random
from Practice4.key_standard.FIPS140_3 import *


def create_blocks(message):
    blocks = []
    if len(message.encode('utf-16')) > 2048:
        for i in range(0, len(message), 2048):
            blocks = blocks[i:i+2048]
    else:
        blocks = [message]

    return blocks


def generate_random_prime_number():
    def Eiler(p):
        return p-1

    bits_sequence = ''
    test_1, test_2, test_3, test_4 = False, False, False, False
    while (test_1 or test_2 or test_3 or test_4) == False:
        bits_sequence = ''.join(random.choice('01') for _ in range(2048, 4096))
        test_1 = monobit_test(bits_sequence)
        test_2 = maximum_length_of_the_series_test(bits_sequence)
        test_3 = pokker_test(bits_sequence)
        test_4 = series_length_test(bits_sequence)
    p = int(bits_sequence, 2)
    g = 0
    while pow(g, Eiler(p), p) != 1:
        g = random.randint(1, 256)

    return p, g


def key_generation(p, g):
    a = random.randint(1, p - 2)
    b = pow(g, a, p)

    return a, b


def encrypt_message(message, p, g, b):
    k = random.randint(1, p - 1)
    x = pow(g, k, p)
    ct = pow(b, k, p)
    y = []
    for block in message:
        for char in block:
            y.append(char)
    for i in range(0, len(y)):
        y[i] = ct * ord(y[i])

    return x, y


def decrypt_message(x, y, a, p):
    s = pow(x, a, p)
    pt = []
    m = ''
    for i in range(0, len(y)):
        pt.append(chr(int(y[i] / s)))
    for char in pt:
        m += char

    return m
