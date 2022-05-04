import unittest
import ibm_ai_modules


class TestEnglFrench(unittest.TestCase): 
    def test3(self): 
        self.assertEqual(ibm_ai_modules.translator.english_to_french('sun'), 'Soleil') 
        self.assertEqual(ibm_ai_modules.translator.english_to_french('Hello'), 'Bonjour')  
        self.assertNotEqual(ibm_ai_modules.translator.english_to_french('car'), 'parapluie') 
        self.assertNotEqual(ibm_ai_modules.translator.english_to_french(0), 0)
        # self.assertIsNotNone(ibm_ai_modules.translator.english_to_french(None),  "Test value is none.")


class TestFrenchEnglish(unittest.TestCase): 
    def test4(self): 
        self.assertEqual(ibm_ai_modules.translator.french_to_english('Soleil'), 'Sun') 
        self.assertEqual(ibm_ai_modules.translator.french_to_english('Bonjour'), 'Hello')  
        self.assertNotEqual(ibm_ai_modules.translator.french_to_english('parapluie'), 'umbrella') 
        # self.assertIsNotNone(ibm_ai_modules.translator.french_to_english(None),  "Test value is none.")
        
class TestEnglFrench_None(unittest.TestCase): 
    def test_NotNone_engl_french(self): 
        self.assertIsNotNone(ibm_ai_modules.translator.english_to_french('geek'),  "Test value is none.")
        
class TestFrenchEnglish_None(unittest.TestCase): 
    def test_NotNone_french_engl(self): 
        self.assertIsNotNone(ibm_ai_modules.translator.french_to_english('geek'),  "Test value is none.")
                       

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=3, exit=False)