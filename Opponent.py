import pygame
from Character import Character

class Opponent(Character):
    def __init__(self, name, health, x, y, is_star=False):
        super().__init__(name, health)
        self.is_star = is_star
        self.x = x  # Posición en el eje X
        self.y = y  # Posición en el eje Y
        self.speed = 5  # Velocidad de movimiento
        self.image = pygame.Surface((50, 50))  # Representación gráfica
        self.image.fill((255, 0, 0))  # Color rojo para el oponente

    def draw(self, screen):
        """Dibuja al oponente en la pantalla."""
        screen.blit(self.image, (self.x, self.y))

    def move(self, direction):
        """Mueve al oponente en la dirección especificada."""
        if direction == "up":
            self.y -= self.speed
        elif direction == "down":
            self.y += self.speed
        elif direction == "left":
            self.x -= self.speed
        elif direction == "right":
            self.x += self.speed
        print(f"{self.name} moves {direction} to ({self.x}, {self.y}).")

    def shoot(self):
        """Lógica de disparo."""
        print(f"{self.name} shoots!")