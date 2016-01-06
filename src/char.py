""" The module takes care of Characters and it's corresponding classes """
class Char:
    """ The class that represents one character and it's behaviour """
    def __init__(self, name, strength, dexterity, hitpoints):
        self.__name = name
        self.__strength = strength
        self.__dexterity = dexterity
        assert hitpoints > 0
        self.__hitpoints = hitpoints

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
        if self.__hitpoints <= 0:
            raise CharacterDead()

    def __str__(self):
        return "<Character name="+self.name()+" strength="+str(self.strength())+" \
        dexterity="+str(self.dexterity())+" hp="+str(self.hitpoints())+">"

class CharacterDead(Exception):
    pass
