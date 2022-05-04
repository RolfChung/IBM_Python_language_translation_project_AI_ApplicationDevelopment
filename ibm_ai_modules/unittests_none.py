import unittest
import ibm_ai_modules

class TestEnglFrench(unittest.TestCase): 
    def test_NotNone_engl_french(self): 
        self.assertIsNotNone(ibm_ai_modules.translator.english_to_french('geek'),  "Test value is not none.")
        
class TestFrenchEnglish(unittest.TestCase): 
    def test_NotNone_french_engl(self): 
        self.assertIsNotNone(ibm_ai_modules.translator.french_to_english('geek'),  "Test value is not none.")
        

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=3, exit=False)