import pygame

class CaveView:

    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    def __init__(self, cave):
        self._cave = cave

    def draw_stick_figure(self, screen, x, y):
        # Head
        pygame.draw.ellipse(screen, self.BLACK, [1 + x, y, 10, 10], 0)

        # Legs
        pygame.draw.line(screen, self.BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
        pygame.draw.line(screen, self.BLACK, [5 + x, 17 + y], [x, 27 + y], 2)

        # Body
        pygame.draw.line(screen, self.RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)

        # Arms
        pygame.draw.line(screen, self.RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
        pygame.draw.line(screen, self.RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)

    def draw_field(self, screen, field, xmin, ymin, xmax, ymax):

        if not field.is_move_north_possible():
            pygame.draw.line(screen, self.BLACK, [xmin, ymin], [xmax, ymin], 1)
        if not field.is_move_south_possible():
            pygame.draw.line(screen, self.BLACK, [xmin, ymax], [xmax, ymax], 1)
        if not field.is_move_east_possible():
            pygame.draw.line(screen, self.BLACK, [xmax, ymin], [xmax, ymax], 1)
        if not field.is_move_west_possible():
            pygame.draw.line(screen, self.BLACK, [xmin, ymin], [xmin, ymax], 1)
        if field.has_char():
            self.draw_stick_figure(screen, xmin+((xmax-xmin) / 2)-5, ymin+((ymax-ymin) / 2)-14)

    def draw(self, screen):
        rownumber = 0
        fields = self._cave.get_map()
        for row in fields:
            columnnumber = 0
            for field in row:
                self.draw_field(screen, field, 50 * columnnumber, 50 * rownumber, 50 * (columnnumber +1) - 1, 50 * (rownumber +1) - 1)
                columnnumber += 1
            rownumber += 1
