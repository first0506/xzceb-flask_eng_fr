import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        englishToFrench('')  # Test for null input for englishToFrench.
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')  # Test for the translation of the world 'Hello' and 'Bonjour'.


class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        frenchToEnglish('') # Test for null input for frenchToEnglish
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # Test for the translation of the world 'Bonjour' and 'Hello'.

unittest.main()