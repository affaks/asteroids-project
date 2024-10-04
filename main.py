import pygame
from constants import *
from player import Player  # Ensure you import the Player class
from circleshape import CircleShape

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create groups
    updatable = pygame.sprite.Group()  # Group for all objects that can be updated
    drawable = pygame.sprite.Group()    # Group for all objects that can be drawn

    # Create a Player instance and add to both groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable.add(player)
    drawable.add(player)

    clock = pygame.time.Clock()

    while True:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game loop

        # Update all updatable objects
        updatable.update(dt)

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Draw all drawable objects
        drawable.draw(screen)

        # Refresh the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
