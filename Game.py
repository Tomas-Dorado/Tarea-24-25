import pygame
from Opponent import Opponent
from Player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Game with Pygame")
        self.clock = pygame.time.Clock()
        self.score = 0
        self.player = Player()  # Asegúrate de implementar la clase Player
        self.opponent = Opponent()  # Asegúrate de implementar la clase Opponent
        self.is_running = False
        self.font = pygame.font.Font(None, 36)

    def start(self):
        self.is_running = True
        self.score = 0
        print("Game started!")

    def update(self):
        if self.is_running:
            self.screen.fill((0, 0, 0))  # Fondo negro
            self.handle_events()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)  # Limitar a 60 FPS
        else:
            print("Game is not running.")

    def end_game(self):
        self.is_running = False
        print("Game ended!")
        pygame.quit()

    def convert_enemy_to_star(self):
        if self.is_running and self.opponent:
            self.score += 1
            print(f"{self.opponent} converted to star! Current score: {self.score}")
            self.opponent = None  # Eliminar al oponente después de la conversión
        elif not self.is_running:
            print("Game is not running. Cannot convert enemy.")
        else:
            print("No opponent to convert.")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.end_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Presionar espacio para convertir enemigo
                    self.convert_enemy_to_star()

    def draw(self):
        # Dibujar jugador, oponente y puntaje
        if self.player:
            self.player.draw(self.screen)
        if self.opponent:
            self.opponent.draw(self.screen)
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

# Ejemplo de uso
if __name__ == "__main__":
    game = Game()
    game.start()
    while game.is_running:
        game.update()