class Field:

    def __init__(self, south = True, north = True, east = True, west = True):
        self._south = south
        self._north = north
        self._east = east
        self._west = west

    def is_move_south_possible(self):
        return self._south

    def is_move_north_possible(self):
        return self._north

    def __str__(self):
        directions = "north," if self._north else ""
        directions += "south," if self._south else ""
        directions += "east," if self._east else ""
        directions += "west" if self._west else ""
        if directions[-1] == ',':
            directions = directions[:-1]
        return "<Field " + directions + ">"
