#!/usr/bin/env python
import unittest
import sys
from carddeck import CardDeck

class TestCardDeck(unittest.TestCase):

    def setUp(self):
        self.d = CardDeck("TEST USER")

    def tearDown(self):
        pass

    def test_deck_len_is_52(self):
        self.assertEqual(52, len(self.d), "Length is not 52")

    def test_drawing_one_card_reduces_length_by_one(self):
        self.d = CardDeck("TEST USER")
        old_len = len(self.d)
        self.d.draw()
        new_len = len(self.d)
        self.assertEqual(1, old_len - new_len, "Draw does not reduce length of deck")

    @classmethod
    def setUpClass(cls):
        pass

    @unittest.skipUnless(sys.platform == 'win32', "only implemented on Windows")
    def test_empty_deck_raises_exception(self):
        with self.assertRaises(ValueError):
            for i in range(53):
                self.d.draw()



if __name__ == '__main__':
    unittest.main(verbosity=11)
