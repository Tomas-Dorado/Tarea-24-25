import pygame
from Entity import Entity

class Character(Entity):
    def __init__(self, x, y, images, lives):
        super().__init__(x,y, images)  # Llamamos al constructor de la clase base
        self.lives = lives
        self.speed = 5  # Velocidad de movimiento

    def move(self, direction):
        # Movimiento basado en la dirección
        if direction == "up":
            self.position.y -= self.speed
        elif direction == "down":
            self.position.y += self.speed
        elif direction == "left":
            self.position.x -= self.speed
        elif direction == "right":
            self.position.x += self.speed
        print(f"Character moves {direction} to position {self.position}")

    def shoot(self):
        # Implementar lógica de disparo (puedes agregar balas o efectos)
        print("Character shoots")

    def collide(self):
        # Lógica de colisión
        self.lives -= 1
        self.is_alive = self.lives > 0
        print(f"Character collided. Lives remaining: {self.lives}")

    def draw(self, screen):
        # Dibujar el personaje en la pantalla
        screen.blit(self.sprite, self.position)
