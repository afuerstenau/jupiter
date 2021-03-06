import unittest
from ..src.model.char import Char
from ..src.model.char import CharacterDead
from ..src.model.combat import Combat

class TestFight(unittest.TestCase):
    fighter1 = Char("Alex", strength=10, dexterity=10, hitpoints=10)
    fighter2 = Char("David", strength=10, dexterity=10, hitpoints=10)

    def test_simple_fight_until_one_fighter_wins(self):
        fighter1 = Char("David", strength=15, dexterity=9, hitpoints=100)
        fighter2 = Char("Mika", strength=15, dexterity=9, hitpoints=100)

        combat = Combat(fighter1, fighter2)
        with self.assertRaises(CharacterDead):
            while True:
                combat.fight()
        self.assertTrue(fighter1.is_dead() != fighter2.is_dead())

    def test_prevent_fight_with_no_hitpoints(self):
        fighter1 = TestFight.fighter1
        fighter2 = TestFight.fighter2
        print("fighter1", fighter1)
        print("fighter2", fighter2)
        try:
            fighter1.receive_damage(10)
        except CharacterDead:
            print("fighter1", fighter1)
            print("fighter2", fighter2)
            with self.assertRaises(AssertionError):
                Combat(fighter1, fighter2)
