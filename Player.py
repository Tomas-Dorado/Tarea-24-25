from Character import Character

class Player(Character):
    def __init__(self, name, score=0, lives=3):
        super().__init__(name)
        self.score = score
        self.lives = lives

    def __str__(self):
        return f"Player {self.name}: Score {self.score}, Lives {self.lives}"
    
    def move(self, direction):
        print(f"{self.name} moves {direction}.")

    def shoot(self):
        print(f"{self.name} shoots!")