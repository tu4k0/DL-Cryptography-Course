from Practice10.ECDSA.ECDSA import *


def main():
    print("Demonstration of Elliptic Curve Digital Signature Algorithm (ECDSA)")
    message = input('\nEnter message: ')
    print("\nStep 1: Keys generation")
    ecdsa_signature = ECDSA()
    ecdsa_signature.key_generation()
    print(f"Private key: {ecdsa_signature.private_key}")
    print(f"Public key: (x={ecdsa_signature.public_key.x}, y={ecdsa_signature.public_key.y})")
    print("\nStep 2: ECDSA sign")
    ecdsa_signature = ECDSA()
    r, s = ecdsa_signature.sign_message(message)
    print(f"Message: {message}")
    print(f"Signature: ({ECDSA.transformIntToHex(r)}, {ECDSA.transformIntToHex(s)})")
    print("\nStep 3: ECDSA verify signature")
    verify_status = ecdsa_signature.verify_signature(message, r, s)
    print(f"Status: {verify_status}")


if __name__ == "__main__":
    main()
