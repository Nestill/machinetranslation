import unittest
from Translate import french_to_english, english_to_french


class MyTestCase(unittest.TestCase):
    def englishToFrench(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # add assertion here
    def frenchToEnglish(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')  # add assertion here


if __name__ == '__main__':
    unittest.main()
