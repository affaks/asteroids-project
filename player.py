import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    containers = (pygame.sprite.Group(), pygame.sprite.Group())

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

        # Create an image for the player
        self.image = pygame.Surface((PLAYER_RADIUS * 2, PLAYER_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (PLAYER_RADIUS, PLAYER_RADIUS), PLAYER_RADIUS)

        # Set the rect attribute
        self.rect = self.image.get_rect(center=(x, y))

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # Draw the player image at the correct position
        screen.blit(self.image, self.rect.topleft)  # Draw the image
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)  # Draw the triangle

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:  # Rotate left
            self.rotate(-dt)
        if keys[pygame.K_d]:  # Rotate right
            self.rotate(dt)
        if keys[pygame.K_w]:  # Move forward
            self.move(dt)
        if keys[pygame.K_s]:  # Move backward
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position -= forward * PLAYER_SPEED * dt

        # Update rect position to follow the player position
        self.rect.center = (self.position.x, self.position.y)
