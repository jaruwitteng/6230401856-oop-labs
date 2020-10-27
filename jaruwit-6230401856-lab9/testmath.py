import unittest
import maths


class Testmath(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(maths.sum(1, 2), 3)
        self.assertEqual(maths.sum(1.1, 2.3), 3.4)

    def test_subtract(self):
        self.assertEqual(maths.substract(10, 2), 8)
        self.assertEqual(maths.substract(-3, 2), -5)

    def test_mul(self):
        self.assertEqual(maths.mul(2, 3), 6)
        self.assertEqual(maths.mul(-1, -2), 2)

    def test_divide(self):
        self.assertEqual(maths.divide(10, 2), 5)
        self.assertEqual(maths.divide(3, 2), 1.5)
        self.assertRaises(ValueError, maths.divide, 12, 0)


if __name__=="__main__":
    unittest.main()


