import unittest

import ps_3_1

class TestPS_3_1(unittest.TestCase):

    def test_case_1(self):
        self.assertAlmostEqual(ps_3_1.radiationExposure(0, 5, 1), 39.10318784326239, places=2)

    def test_case_2(self):
        self.assertAlmostEqual(ps_3_1.radiationExposure(5, 11, 1), 22.94241041057671, places=2)

    def test_case_3(self):
        self.assertAlmostEqual(ps_3_1.radiationExposure(0, 11, 1), 62.0455982538, places=2)

    def test_case_4(self):
        self.assertAlmostEqual(ps_3_1.radiationExposure(40, 100, 1.5), 0.434612356115, places=2)

if __name__ == '__main__':
    unittest.main()
