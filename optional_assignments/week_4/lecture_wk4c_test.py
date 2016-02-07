import unittest

import lecture_wk4c

class TestNFruits(unittest.TestCase):
    
    # Example Test
    def test_case_1(self):
        self.assertEqual(lecture_wk4c.nfruits({'A': 1, 'B': 2, 'C': 3}, 'AC'), 3)
        
    # 1 Fruit
    def test_case_2(self):
        self.assertEqual(lecture_wk4c.nfruits({'A': 1}, 'A'), 0)
        
    # 2 fruits, 1 each   
    def test_case_3(self):
        self.assertEqual(lecture_wk4c.nfruits({'A': 1, 'B': 1}, 'AB'), 1)
        
    # 2 fruits, eat 1 only    
    def test_case_4(self):
        self.assertEqual(lecture_wk4c.nfruits({'A': 1, 'B': 1}, 'A'), 1)
        
if __name__ == '__main__':
    unittest.main()