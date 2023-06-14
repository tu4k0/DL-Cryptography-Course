import random
from Practice5.hashing_algorithms.SHA1_own import SHA1_own
from Practice4.key_standard.FIPS140_3 import *


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


def sign_message(p, g, a, message):
    s = 0
    r = 0
    m = 0
    while s == 0:
        k = random.randint(1, p - 1)
        r = pow(g, k, p)
        m = int(SHA1_own(message), 16)
        s = ((m - a * r) * 1 // k) % (p - 1)

    return r, s, m


def check_signature(p, g, b, r, s, m):
    y = (1 // b) % p
    u1 = m * (1 // s) % (p - 1)
    u2 = (r * 1 // s) % (p - 1)
    v = (pow(g, u1) * pow(y, u2)) % p
    if v == r:
        return True
    else:
        return False



