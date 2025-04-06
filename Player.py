import pygame
from Character import Character

class Player(Character):
    def __init__(self, x=0, y=0, score=0, lives=3):
        super().__init__(name="Player1")  # Default name for the player
        self.x = x
        self.y = y
        self.score = score
        self.lives = lives
        self.speed = 5  # Movement speed

    def __str__(self):
        return f"Player {self.name}: Score {self.score}, Lives {self.lives}, Position ({self.x}, {self.y})"
    
    def move(self, keys):
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

    def shoot(self):
        print(f"{self.name} shoots!")

    def draw(self, screen):
        # Draw the player as a rectangle (example)
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 50, 50))