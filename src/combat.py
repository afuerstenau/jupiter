import random

class Combat:
    def __init__(self, fighter1, fighter2):
        assert fighter1.hitpoints() > 0
        assert fighter2.hitpoints() > 0
        self.__fighter1 = fighter1
        self.__fighter2 = fighter2

    def fight(self):
        attack1 = random.randrange(self.__fighter1.strength())
        attack1 -= self.__fighter2.dexterity()-self.__fighter1.dexterity()
        self.__fighter2.receive_damage(attack1)
        attack2 = random.randrange(self.__fighter2.strength())
        attack2 -= self.__fighter1.dexterity()-self.__fighter2.dexterity()
        self.__fighter1.receive_damage(attack1)
