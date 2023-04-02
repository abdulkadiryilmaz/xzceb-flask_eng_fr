import os
import sys

import unittest



# Get the absolute path of the directory containing the test file
test_dir = os.path.dirname(os.path.abspath(__file__))

# Get the absolute path of the directory containing the package
package_dir = os.path.join(test_dir, "..")

# Add the package directory to sys.path
sys.path.append(package_dir)

import translator

class TestTranslator(unittest.TestCase):

    def test_french_to_english_null_input(self):
        with self.assertRaises(ValueError):
            result = translator.french_to_english(None)

    def test_english_to_french_null_input(self):
        with self.assertRaises(ValueError):
            result = translator.english_to_french(None)

    def test_french_to_english(self):
        result = translator.french_to_english('Bonjour')
        self.assertEqual(result, 'Hello')

    def test_english_to_french(self):
        result = translator.english_to_french('Hello')
        self.assertEqual(result, 'Bonjour')
    
if __name__ == '__main__':
    unittest.main()