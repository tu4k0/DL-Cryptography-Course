from typing import Tuple, Any

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from ecpy.curves import Curve, Point


class EcPoint:
    x: int = 0
    y: int = 0


class ElipticCurve:
    EcPoint: EcPoint
    curve: ec.SECP256K1
    p: int
    formula: bool

    def __init__(self):
        self.EcPoint = EcPoint()
        self.curve = ec.SECP256K1()
        self.a = 0
        self.b = 7
        self.p = pow(2, 256) - pow(2, 32) - 977

    def generate_EC_point(self) -> EcPoint:
        private_key = ec.generate_private_key(self.curve)
        public_key = private_key.public_key()
        self.EcPoint.x = public_key.public_numbers().x
        self.EcPoint.y = public_key.public_numbers().y

        return (self.EcPoint.x, self.EcPoint.y)

    def is_on_curve(self):
        if (self.EcPoint.y ** 2) % self.p == (self.EcPoint.x ** 3 + self.a * self.EcPoint.x + self.b) % self.p:
            return True
        else:
            return False

    def add_EC_points(self, a: EcPoint, b: EcPoint) -> EcPoint:
        if a != b:
            m = (b.EcPoint.y - a.EcPoint.y) / (b.EcPoint.x - a.EcPoint.x)
            self.EcPoint.x = m ** 2 - a.EcPoint.x - b.EcPoint.x
            self.EcPoint.y = m * (a.EcPoint.x - self.EcPoint.x) - a.EcPoint.y
        else:
            self.EcPoint.x = pow((3 * pow(a.EcPoint.x, 2) + self.a) / (2 * a.EcPoint.y), 2) - a.EcPoint.x - a.EcPoint.x
            self.EcPoint.y = ((3 * pow(a.EcPoint.x, 2) + self.a) / (2 * a.EcPoint.y)) * (
                        a.EcPoint.x - self.EcPoint.x) - a.EcPoint.y

        return self.EcPoint

    def double_EC_point(self, a: EcPoint) -> EcPoint:
        self.EcPoint.x = (3 * pow(a.EcPoint.x, 2) / 2 * a.EcPoint.y) - 2 * a.EcPoint.x
        self.EcPoint.y = (3 * pow(a.EcPoint.x, 2) / 2 * a.EcPoint.y) * (a.EcPoint.x - self.EcPoint.x) - a.EcPoint.y

        return self.EcPoint

    def scalar_EC_point(self, k: int, a: EcPoint) -> EcPoint:
        while k > 0:
            if k % 2 == 1:
                self.add_EC_points(a, a)
            self.add_EC_points(a, a)
            k //= 2

        return self.EcPoint

    @staticmethod
    def EC_point_to_string(a: EcPoint) -> Tuple[Any, Any]:
        return (a.EcPoint.x, a.EcPoint.y)

    @staticmethod
    def string_to_EC_point(string: str) -> EcPoint:
        coordinates = string.split(',')
        point = EcPoint()
        point.x = coordinates[0]
        point.y = coordinates[1]

        return point

    @staticmethod
    def print_EC_point(point: EcPoint):
        print(f"X: {point.EcPoint.x}\nY: {point.EcPoint.y}")
