class Char:
    def __init__(self, name, strength, dexterity, hitpoints):
        self.__name=name
        self.__strength=strength
        self.__dexterity=dexterity
        assert hitpoints >0
        self.__hitpoints=hitpoints

    def name(self):
        return self.__name

    def strength(self):
        return self.__strength

    def dexterity(self):
        return self.__dexterity

    def hitpoints(self):
        return self.__hitpoints

    def receive_damage(self, damage):
        self.__hitpoints -= damage
        if self.__hitpoints < 0:
            raise CharacterDead()

class CharacterDead (Exception):
    pass
