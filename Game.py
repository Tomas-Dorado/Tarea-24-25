class Game:
    def __init__(self):
        self.score = 0
        self.player = None
        self.opponent = None
        self.is_running = False

    def start(self):
        self.is_running = True
        self.score = 0
        print("Game started!")

    def update(self):
        if self.is_running:
            print("Game is updating...")
            # Add game logic here
        else:
            print("Game is not running.")

    def end_game(self):
        self.is_running = False
        print("Game ended!")