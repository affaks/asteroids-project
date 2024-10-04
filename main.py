import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create groups for managing sprites
    updatable = pygame.sprite.Group()  # Group for objects that can be updated
    drawable = pygame.sprite.Group()   # Group for objects that can be drawn
    
    # Create a player instance and add it to both groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable.add(player)   # Add player to updatable group
    drawable.add(player)    # Add player to drawable group

    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000  # Calculate delta time

        # Update all objects in the updatable group
        updatable.update(dt)

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw all objects in the drawable group
        drawable.draw(screen)

        # Flip the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
