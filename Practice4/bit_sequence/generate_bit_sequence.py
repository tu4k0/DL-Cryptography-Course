import random


def generate_bit_sequence():
    bits_sequence = ''.join(random.choice('01') for _ in range(20000))

    return bits_sequence
