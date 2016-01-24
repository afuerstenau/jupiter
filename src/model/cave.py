from .field import Field
from .char import Char

class Cave:

    def __init__(self):
        self._map = [[Field(north = False, west = False), Field(north = False, east=False)], \
        [Field(south = False, west = False), Field(south = False, east = False)]]
        self._move_party_to_entrance()

    def _move_party_to_entrance(self):
        self._current_party_field_x = 0
        self._current_party_field_y = 0
        self._current_party_field = self._map[0][0]
        self._current_party_field.set_has_char(True)

        self._map[1][1].set_has_monster(Char.Goblin)

    def move_party(self):
        self._current_party_field.set_has_char(False)
        self._current_party_field =self._map[self._current_party_field_y][self._current_party_field_x]
        self._current_party_field.set_has_char(True)

    def move_party_south(self):
        if not self._current_party_field.is_move_south_possible():
            raise Movement_Not_Possible()
        self._current_party_field_y += 1
        self.move_party()

    def move_party_north(self):
        if not self._current_party_field.is_move_north_possible():
            raise Movement_Not_Possible()
        self._current_party_field_y -= 1
        self.move_party()

    def move_party_east(self):
        if not self._current_party_field.is_move_east_possible():
            raise Movement_Not_Possible()
        self._current_party_field_x += 1
        self.move_party()

    def move_party_west(self):
        if not self._current_party_field.is_move_west_possible():
            raise Movement_Not_Possible()
        self._current_party_field_x -= 1
        self.move_party()

    def get_map(self):
        return self._map

class Movement_Not_Possible(Exception):
    pass
