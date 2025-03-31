from Entity import Entity

class Character(Entity):
    def __init__(self, lives):
        super().__init__()
        self.lives = lives
        self.is_alive = lives > 0

    def move(self, direction):
        # Implement movement logic here
        print(f"Character moves {direction}")

    def shoot(self):
        # Implement shooting logic here
        print("Character shoots")

    def collide(self):
        # Implement collision logic here
        self.lives -= 1
        self.is_alive = self.lives > 0
        print(f"Character collided. Lives remaining: {self.lives}")
