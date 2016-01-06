import unittest
from ..src.char import *
from ..src.combat import Combat

class TestFight(unittest.TestCase):

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
        self.assertTrue((fighter1.hitpoints() < 0) != (fighter2.hitpoints() < 0))
