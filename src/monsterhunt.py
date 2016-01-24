"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
"""

import pygame
from model.cave import Cave
from view.cave_view import CaveView

# Define some colors

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Setup
pygame.init()

# Set the width and height of the screen [width,height]
size = [100, 100]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Monsterjagd")
cave = Cave()
cave_view = CaveView(cave)


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Hide the mouse cursor
pygame.mouse.set_visible(0)

# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            # User pressed down on a key

        elif event.type == pygame.KEYDOWN:
            try:
                if event.key == pygame.K_LEFT:
                    cave.move_party_west()
                elif event.key == pygame.K_RIGHT:
                    cave.move_party_east()
                elif event.key == pygame.K_UP:
                    cave.move_party_north()
                elif event.key == pygame.K_DOWN:
                    cave.move_party_south()
            except Exception as e:
                print(e)


    # --- Game Logic

    # Move the object according to the speed vector.

    # --- Drawing Code

    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    cave_view.draw(screen)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
