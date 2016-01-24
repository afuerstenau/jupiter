"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
"""

import pygame
from model.cave import Cave

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)

    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)

    # Body
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)

    # Arms
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)

def draw_field(screen, field, xmin, ymin, xmax, ymax):
    if not field.is_move_north_possible():
        pygame.draw.line(screen, BLACK, [xmin, ymin], [xmax, ymin], 1)
    if not field.is_move_south_possible():
        pygame.draw.line(screen, BLACK, [xmin, ymax], [xmax, ymax], 1)
    if not field.is_move_east_possible():
        pygame.draw.line(screen, BLACK, [xmax, ymin], [xmax, ymax], 1)
    if not field.is_move_west_possible():
        pygame.draw.line(screen, BLACK, [xmin, ymin], [xmin, ymax], 1)
    if field.has_char():
        draw_stick_figure(screen, xmin+((xmax-xmin) / 2)-5, ymin+((ymax-ymin) / 2)-14)

def draw_fields(screen, fields):
    rownumber = 0
    for row in fields:
        columnnumber = 0
        for field in row:
            draw_field(screen, field, 50 * columnnumber, 50 * rownumber, 50 * (columnnumber +1) - 1, 50 * (rownumber +1) - 1)
            columnnumber += 1
        rownumber += 1

# Setup
pygame.init()

# Set the width and height of the screen [width,height]
size = [100, 100]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Monsterjagd")

cave = Cave()
fields = cave.get_map()

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Hide the mouse cursor
pygame.mouse.set_visible(0)

# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = 10
y_coord = 10

# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            # User pressed down on a key

        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                try:
                    cave.move_party_west()
                except Exception as e:
                    print ("west not possible")
            elif event.key == pygame.K_RIGHT:
                try:
                    cave.move_party_east()
                except Exception as e:
                    print ("east not possible")
            elif event.key == pygame.K_UP:
                try:
                    cave.move_party_north()
                except Exception as e:
                    print ("north not possible")
            elif event.key == pygame.K_DOWN:
                try:
                    cave.move_party_south()
                except Exception as e:
                    pass

    # --- Game Logic

    # Move the object according to the speed vector.

    # --- Drawing Code

    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    draw_fields(screen, fields)


    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
