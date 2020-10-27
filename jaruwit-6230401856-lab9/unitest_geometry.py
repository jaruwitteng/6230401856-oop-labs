import unittest
from geometry import area
from geometry import shape


class Test(unittest.TestCase):
    def testcircle(self):
        self.assertEqual(round(area.get_circle_area(3), 2), 28.27)
        self.assertEqual(area.get_rectangle_area(3, 4), 12)
    def testrectangle(self):
        self.assertEqual(round(area.get_rectangle_area(3,), 2), 28.27)
        self.assertEqual(area.get_rectangle_area(3, 4), 12)


if __name__ == "__main__":
    unittest.main()