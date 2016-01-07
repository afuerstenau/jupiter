from field import Field

class Cave:

    def __init__(self):
        self._map = [[Field(north = False, west = False), Field(north = False, east=False)], \
        [Field(south = False, west = False), Field(south = False, east = False)]]
        self._move_party_to_entrance()

    def _move_party_to_entrance(self):
        self._current_party_field_x = 0
        self._current_party_field_y = 0
        self._current_party_field = self._map[0][0]

    def move_party_south(self):
        print("move_party_south Field 1", self._current_party_field)
        if not self._current_party_field.is_move_south_possible():
            raise Movement_Not_Possible()
        self._current_party_field =self._map[self._current_party_field_y + 1][self._current_party_field_x]
        print("move_party_south Field 2", self._current_party_field)

class Movement_Not_Possible(Exception):
    pass
