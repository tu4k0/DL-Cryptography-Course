from Practice9.ECDH.ECDH import *
from Practice5.hashing_algorithms.SHA1_own import *


def main():
    print("Generation of a secret for two participants (Alice, Bob) in the ECDH protocol")
    print("\nStep 1: Private key generation")
    Alice = Person()
    Bob = Person()
    Alice.private_key = generate_private_key()
    Bob.private_key = generate_private_key()
    print(f"Alice private key:\t\t{Alice.private_key.private_numbers().private_value}")
    print(f"Bob private key:\t\t{Bob.private_key.private_numbers().private_value}")
    print("\nStep 2: Compute eliptic curve point (public key) with curve secp256k1")
    Alice.public_key = compute_public_key(Alice.private_key)
    Bob.public_key = compute_public_key(Bob.private_key)
    print(f"Alice:\t({Alice.public_key.x}, {Alice.public_key.y})")
    print(f"Bob:\t({Bob.public_key.x}, {Bob.public_key.y})")
    print("\nStep 3: Public keys exchanging")
    print(f"Exchange status: ", exchange_public_keys(Alice, Bob))
    ec = ElipticCurve()
    print("\nStep 4: Shared secret computation for Alice")
    Alice.shared_secret = compute_shared_secret(ec, Alice)
    print(f"Resulting Alice shared secret: {Alice.shared_secret.x}")
    print("\nStep 5: Shared secret computation for Bob")
    Bob.shared_secret = compute_shared_secret(ec, Bob)
    print(f"Resulting Alice shared secret: {Bob.shared_secret.x}")
    print("\nStep 6: Compare shared secrets for equality")
    print(f"Result: {compare_shared_secrets(Alice, Bob)}")


if __name__ == "__main__":
    main()
