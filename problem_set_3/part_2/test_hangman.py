import unittest

import ps3_hangman

class TestIsWordGuessed(unittest.TestCase):
    
    def test_case_1(self):
        self.assertTrue(ps3_hangman.isWordGuessed('hello', 'alksjdfasfhello'))
        
    def test_case_2(self):
        self.assertFalse(ps3_hangman.isWordGuessed('hellow', 'alksjdfasfhello'))
        
    def test_case_3(self):
        self.assertTrue(ps3_hangman.isWordGuessed('a', 'a'))
        
    def test_case_4(self):
        self.assertTrue(ps3_hangman.isWordGuessed('1111', '1111'))
        
    def test_case_5(self):
        self.assertTrue(ps3_hangman.isWordGuessed('', ''))
        
class TestGetGuessedWord(unittest.TestCase):
    
    def test_case_1(self):
        self.assertEquals(ps3_hangman.getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's']), '_ pp_ e')

class TestGetAvailableLetters(unittest.TestCase):
    
     def test_case_1(self):
         self.assertEquals(ps3_hangman.getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']), 'abcdfghjlmnoqtuvwxyz')     
                        
if __name__ == '__main__':
    unittest.main()
    