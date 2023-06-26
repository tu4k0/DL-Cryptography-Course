from Practice8.eliptic_curve.ElipticCurve import EcPoint, ElipticCurve
from ecpy.curves import Curve, Point

def main():
    a = ElipticCurve()
    b = ElipticCurve()
    a.generate_EC_point()
    b.generate_EC_point()
    print(f"Eliptic curve: {a.curve.name}\n")
    print("Point a data: ")
    ElipticCurve.print_EC_point(a)
    print("\n")
    print("Point b data: ")
    ElipticCurve.print_EC_point(b)
    print("\n")
    print(f"a is on curve status (True-Yes, False-No): {a.is_on_curve()}\n")
    c = ElipticCurve()
    c.add_EC_points(a, b)
    print("Point c (as a result of point a + point b addition) data: ")
    ElipticCurve.print_EC_point(c)


if __name__ == "__main__":
    main()