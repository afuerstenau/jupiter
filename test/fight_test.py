import unittest
from ..src.char import Char
from ..src.char import CharacterDead
from ..src.combat import Combat

class TestFight(unittest.TestCase):
    fighter1 = Char("Alex", strength=10, dexterity=10, hitpoints=10)
    fighter2 = Char("David", strength=10, dexterity=10, hitpoints=10)

    def test_simple_fight_one_round(self):
        fighter1 = Char("David", strength=15, dexterity=9, hitpoints=100)
        fighter2 = Char("Alex", strength=15, dexterity=9, hitpoints=100)

        combat = Combat(fighter1, fighter2)
        combat.fight()

        self.assertTrue(fighter2.hitpoints() <= 100)

    def test_simple_fight_until_one_fighter_wins(self):
        fighter1 = Char("David", strength=15, dexterity=9, hitpoints=100)
        fighter2 = Char("Alex", strength=15, dexterity=9, hitpoints=100)

        combat = Combat(fighter1, fighter2)
        with self.assertRaises(CharacterDead):
            while True:
                combat.fight()
        self.assertTrue((fighter1.hitpoints() <= 0) != (fighter2.hitpoints() <= 0))

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
