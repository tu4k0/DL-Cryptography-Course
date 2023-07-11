import random
import re
import string

from Practice5.hashing_algorithms.SHA1_own import SHA1_own
from Practice8.eliptic_curve import ElipticCurve
from Practice9.ECDH import ECDH


class ECDSA(ElipticCurve.ElipticCurve):
    curve: str = None
    private_key: int = None
    public_key: ElipticCurve.EcPoint = ElipticCurve.EcPoint()
    base_point: ElipticCurve.EcPoint = ElipticCurve.EcPoint()
    signature: list

    def __init__(self):
        super().__init__()
        private_key = ElipticCurve.ec.generate_private_key(ElipticCurve.ec.SECP256K1(), ElipticCurve.default_backend())
        public_key = private_key.public_key()
        self.curve = public_key.public_numbers().curve.name
        self.base_point.x = public_key.public_numbers().x
        self.base_point.y = public_key.public_numbers().y
        self.private_key = 0
        self.public_key.x = 0
        self.public_key.y = 0

    def setCurve(self, curve):
        self.curve = curve

    def setBasePoint(self, point):
        self.base_point = point

    def getCurve(self):
        return self.curve

    def getPrivateKey(self):
        return self.private_key

    def getPublicKey(self):
        return self.public_key

    def getSignature(self):
        return self.signature

    def key_generation(self):
        private_key = ECDH.generate_private_key()
        self.private_key = private_key.private_numbers().private_value
        self.public_key.x = ECDSA.transformIntToHex(ECDH.compute_public_key(private_key).x)
        self.public_key.y = ECDSA.transformIntToHex(ECDH.compute_public_key(private_key).y)

        return self.private_key, self.public_key

    def sign_message(self, message):
        h = int(SHA1_own(message), 16)
        k = random.randint(1, ECDH.P-1)
        ec = ElipticCurve.ElipticCurve()
        r = ec.scalar_EC_point(k, self.base_point)
        s = (pow(k, -1) * (h + r.x * self.private_key)) % self.p
        self.signature = [r.x, s]

        return self.signature

    def verify_signature(self, message, r, s):
        h = int(SHA1_own(message), 16)
        s1 = (pow(s, -1)) % self.p
        ec = ElipticCurve.ElipticCurve()
        R = ec.scalar_EC_point(h * s1, self.base_point)
        if R.x == r:
            return True
        else:
            return False

    @staticmethod
    def transformIntToHex(value):
        return SHA1_own(str(value))
