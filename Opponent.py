from Character import Character

class Opponent(Character):
    def __init__(self, name, health, is_star=False):
        super().__init__(name, health)
        self.is_star = is_star

    def move(self, direction):
        # Implement movement logic
        print(f"{self.name} moves {direction}.")

    def shoot(self):
        # Implement shooting logic
        print(f"{self.name} shoots!")