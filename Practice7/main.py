from Practice7.digital_signature.Elgamal import *


def main():
    message = input('Enter message: ')
    p, q = generate_random_prime_number()
    a, b = key_generation(p, q)
    print(f"\nKeys: \nPublic: {b}\nPrivate: {a}")
    r, s, m = sign_message(p, q, a, message)
    print(f"\nSignature:\n({r}, {s})")
    verification_status = check_signature(p, q, b, r, s, m)
    print(f"\nVerification Status: {verification_status}")


if __name__ == '__main__':
    main()