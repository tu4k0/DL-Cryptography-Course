from Practice7.digital_signature.Elgamal_signature import *
from Practice7.encryption.Elgamal_encryption import *


def elgamal_signature(message):
    p, q = generate_random_prime_number()
    a, b = key_generation(p, q)
    print(f"\nKeys: \nPublic: {b}\nPrivate: {a}")
    r, s, m = sign_message(p, q, a, message)
    print(f"\nSignature:\n({r}, {s})")
    verification_status = check_signature(p, q, b, r, s, m)
    print(f"\nVerification Status: {verification_status}")


def elgamal_encryption(message):
    blocks = create_blocks(message)
    p, g = generate_random_prime_number()
    a, b = key_generation(p, g)
    print(f"\nKeys: \nPublic: {b}\nPrivate: {a}")
    x, y = encrypt_message(blocks, p, g, b)
    print(f"\nCiphertext:\n({x}, {y})")
    m = decrypt_message(x, y, a, p)
    print(f"\nPlaintext:\n{m}")


if __name__ == '__main__':
    mode = input('Choose Elgamal mode (signature/encryption): ')
    message = input('Enter message: ')
    if mode == 'signature':
        elgamal_signature(message)
    elif mode == 'encryption':
        elgamal_encryption(message)

