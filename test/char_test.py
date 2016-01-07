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

    def test_prevent_create_dead_char(self):
        with self.assertRaises(AssertionError):
            Char(TestChar.name, strength=TestChar.strength, dexterity=TestChar.dexterity, hitpoints=0)

    def test_str_method(self):
        char = Char(TestChar.name, strength=TestChar.strength, dexterity=TestChar.dexterity, hitpoints=1)
        self.assertEqual(str(char), "<Character name="+TestChar.name+" strength="+str(TestChar.strength)+" dexterity="+str(TestChar.dexterity)+" hp=1>")

    def test_calculate_and_get_attack_power(self):
        char = self.testchar
        for _ in range(10):
            attack_power = char.calculate_and_get_attack_power()
            print("attack power:", attack_power)
            self.assertTrue(0 <= attack_power < 19)

    def test_calculate_and_get_defending_power(self):
        char = self.testchar
        for _ in range(10):
            defending_power = char.calculate_and_get_defending_power()
            self.assertTrue(isinstance(defending_power, int))
            print("defending power:", defending_power)
            self.assertTrue(0 <= defending_power <= 9)

    def test_is_alive(self):
        char = self.create_testchar()
        self.assertTrue(char.is_alive())

    def test_is_dead(self):
        char = self.create_testchar()
        try:
            char.receive_damage(self.hitpoints)
        except Exception as e:
            pass
        self.assertTrue(char.is_dead())

    def create_testchar(self):
        return Char(self.name, strength=self.strength, dexterity=self.dexterity, \
        hitpoints=self.hitpoints)
