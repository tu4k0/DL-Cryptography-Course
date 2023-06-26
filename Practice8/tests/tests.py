import unittest

from Practice8.eliptic_curve.ElipticCurve import EcPoint, ElipticCurve


class Tests(unittest.TestCase):

    def test_point_on_curve(self):
        a = ElipticCurve()
        a.generate_EC_point()
        self.assertTrue(True, a.is_on_curve())

    def test_point_generation(self):
        x = 0
        y = 0
        a = ElipticCurve()
        a.generate_EC_point()
        self.assertFalse(False, a.EcPoint.x != x)
        self.assertFalse(False, a.EcPoint.y != y)

    def test_add_two_points(self):
        x = -7.797792383190269e+76
        y = 6.8568878338604e+76
        a = ElipticCurve()
        a.EcPoint.x = 29830335924900656389752366697690257568481349701634126709796668727375685460265
        a.EcPoint.y = 23979494680709277187752216340251764425718426247921436533215270642477504297730
        b = ElipticCurve()
        b.EcPoint.x = 48147587907002044313434261642833880058028432107262210890561632256588073672586
        b.EcPoint.y = 39704002922957341255946303834732727295282061468769393750846689986900114928939
        c = ElipticCurve()
        c.add_EC_points(a, b)
        self.assertEqual(c.EcPoint.x, x)
        self.assertEqual(c.EcPoint.y, y)


if __name__ == "__main__":
    unittest.main()
