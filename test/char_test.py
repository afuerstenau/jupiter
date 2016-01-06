import unittest
from ..src.char import *

class TestChar(unittest.TestCase):
    name = "David"
    strength = 18
    dexterity = 9
    hitpoints = 50
    def test_create_simple_char_with_attributes(self):
        name = "David"
        dex=9
        strength=15
        simple_char = Char(name, strength=strength, dexterity=dex, hitpoints=50)
        self.assertEqual(simple_char.name(), name)
        self.assertEqual(simple_char.strength(), strength)
        self.assertEqual(simple_char.dexterity(), dex)
        simple_char.__dexterity=15
        self.assertEqual(simple_char.dexterity(), dex)

    def test_character_dies(self):
        simple_char = Char(TestChar.name, strength=TestChar.strength, dexterity=TestChar.dexterity, hitpoints=TestChar.hitpoints)
        with self.assertRaises(CharacterDead):
            simple_char.receive_damage(51)

    def test_prevent_create_char_with_no_hitpoints(self):
        with self.assertRaises(AssertionError):
            Char(TestChar.name, strength=TestChar.strength, dexterity=TestChar.dexterity, hitpoints=0)
