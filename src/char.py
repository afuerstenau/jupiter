""" The module takes care of Characters and it's corresponding classes """
import random

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

    def receive_damage(self, damage):
        self.__hitpoints -= damage
        if self.__hitpoints <= 0:
            raise CharacterDead()

    def is_alive(self):
        print("is_alive", self.__hitpoints, (self.__hitpoints > 0))
        return self.__hitpoints > 0

    def is_dead(self):
        return self.__hitpoints <= 0

    def __str__(self):
        return "<Character name="+self.name()+" strength="+str(self.strength())+" dexterity="+str(self.dexterity())+" hp="+str(self.__hitpoints)+">"

    def calculate_and_get_attack_power(self):
        return random.randint(0, self.strength())

    def calculate_and_get_defending_power(self):
        defending_power = random.normalvariate(self.dexterity()/2, self.dexterity()/2)
        if defending_power < 0:
            return 0
        elif defending_power > self.dexterity():
            return self.dexterity()
        else:
            return int(defending_power)

class CharacterDead(Exception):
    pass
