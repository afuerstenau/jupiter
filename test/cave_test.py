import unittest
from ..src.model.char import Char
from ..src.model.cave import Cave
from ..src.model.cave import Movement_Not_Possible

class TestCave(unittest.TestCase):
    name = "David"
    strength = 18
    dexterity = 9
    hitpoints = 50
    testchar = Char(name, strength=strength, dexterity=dexterity, hitpoints=hitpoints)

    def test_create_cave(self):
        Cave()


    def test_move_south_possible(self):
        cave = Cave()
        cave.move_party_south()

    def test_move_south_blocked(self):
        cave = Cave()
        cave.move_party_south()
        with self.assertRaises(Movement_Not_Possible):
            cave.move_party_south()
