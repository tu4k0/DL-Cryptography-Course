from Practice8.eliptic_curve.ElipticCurve import *


# Constants
# Curve definition
CURVE = ec.SECP256K1()

# Parameters
A = 0
B = 7
P = pow(2, 256) - pow(2, 32) - 977


class Person:
    private_key: int = None
    public_key: EcPoint = None
    shared_secret: EcPoint.x = None


def generate_private_key():
    private_key = ec.generate_private_key(CURVE)

    return private_key


def compute_public_key(private_key):
    public_key = private_key.public_key()
    ec_point = EcPoint()
    ec_point.x = public_key.public_numbers().x
    ec_point.y = public_key.public_numbers().y

    return ec_point


def exchange_public_keys(person_1: Person, person_2: Person):
    person_1.public_key_initial = person_1.public_key
    person_2.public_key_initial = person_2.public_key
    person_1.public_key, person_2.public_key = person_2.public_key, person_1.public_key
    if person_1.public_key != person_1.public_key_initial and person_2.public_key != person_2.public_key_initial:
        return True
    else:
        return False


def compare_shared_secrets(person_1: Person, person_2: Person):
    if person_1.shared_secret and person_2.shared_secret:
        if person_1.shared_secret.x == person_2.shared_secret.x:
            return True
        else:
            return False
    else:
        raise Exception('Person 1 and Person 2 don`t have shared secrets at the moment')
