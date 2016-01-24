class Field:

    def __init__(self, south = True, north = True, east = True, west = True, has_char = False):
        self._south = south
        self._north = north
        self._east = east
        self._west = west
        self._has_char = has_char
        self._monster = ""

    def is_move_south_possible(self):
        return self._south

    def is_move_north_possible(self):
        return self._north

    def is_move_east_possible(self):
        return self._east

    def is_move_west_possible(self):
        return self._west

    def has_char(self):
        return self._has_char

    def set_has_char(self, has_char):
        self._has_char = has_char

    def set_has_monster(self, monster):
        self._monster = monster

    def get_monster(self):
        return self._monster

    def __str__(self):
        directions = "north," if self._north else ""
        directions += "south," if self._south else ""
        directions += "east," if self._east else ""
        directions += "west" if self._west else ""
        if directions[-1] == ',':
            directions = directions[:-1]
        return "<Field " + directions + ">"
