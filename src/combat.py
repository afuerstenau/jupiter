
class Combat:
    def __init__(self, fighter1, fighter2):
        assert fighter1.is_alive()
        assert fighter2.is_alive()
        self.__fighter1 = fighter1
        self.__fighter2 = fighter2

    def fight(self):
        attack1 = self.__fighter1.calculate_and_get_attack_power()
        attack1 -= self.__fighter2.calculate_and_get_defending_power()
        self.__fighter2.receive_damage(attack1)
        attack2 = self.__fighter2.calculate_and_get_attack_power()
        attack2 -= self.__fighter1.calculate_and_get_defending_power()
        self.__fighter1.receive_damage(attack1)
