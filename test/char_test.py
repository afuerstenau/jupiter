import unittest
from ..src.char import Char
from ..src.char import CharacterDead

class TestChar(unittest.TestCase):

    name = "David"
    strength = 18
    dexterity = 9
    hitpoints = 50
    testchar = Char(name, strength=strength, dexterity=dexterity, hitpoints=hitpoints)
    def test_create_simple_char_with_attributes(self):
        simple_char = self.testchar
        self.assertEqual(simple_char.name(), self.name)
        self.assertEqual(simple_char.strength(), self.strength)
        self.assertEqual(simple_char.dexterity(), self.dexterity)
        simple_char.__dexterity = 15
        self.assertEqual(simple_char.dexterity(), self.dexterity)

    def test_character_dies(self):
        simple_char = self.testchar
        with self.assertRaises(CharacterDead):
            simple_char.receive_damage(50)

    def test_prevent_create_char_with_no_hitpoints(self):
        with self.assertRaises(AssertionError):
            Char(TestChar.name, strength=TestChar.strength, dexterity=TestChar.dexterity, hitpoints=0)

    def test_str_method(self):
        char = Char(TestChar.name, strength=TestChar.strength, dexterity=TestChar.dexterity, hitpoints=1)
        self.assertEqual(str(char), "<Character name="+TestChar.name+" strength="+str(TestChar.strength)+" dexterity="+str(TestChar.dexterity)+" hp=1>")
