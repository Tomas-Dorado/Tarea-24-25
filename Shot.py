import pygame
from Entity import Entity

class Shot(Entity):
    def __init__(self, x, y, speed, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed

    def move(self):
        # Move the shot upwards
        self.rect.y -= self.speed

    def hit_target(self, target):
        # Check if the shot collides with the target
        return self.rect.colliderect(target.rect)

    def draw(self, screen):
        # Draw the shot on the screen
        screen.blit(self.image, self.rect)