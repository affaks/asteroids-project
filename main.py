import pygame
from constants import *

def main():
    # Initialize pygame
    pygame.init()

    # Create a window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while True:
        # Check for user events (like closing the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game loop

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Refresh the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
