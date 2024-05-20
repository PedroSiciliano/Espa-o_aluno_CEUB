import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definições de cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Configurações da janela
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
PACMAN_SPEED = 5

# Definição de direções
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Classe do Pac-Man
class Pacman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([GRID_SIZE, GRID_SIZE])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.direction = RIGHT
        self.speed = PACMAN_SPEED

    def update(self):
        self.rect.move_ip((self.direction[0] * self.speed, self.direction[1] * self.speed))

# Classe do jogo
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pac-Man")
        self.clock = pygame.time.Clock()
        self.pacman = Pacman()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.pacman)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.pacman.direction = LEFT
            elif keys[pygame.K_RIGHT]:
                self.pacman.direction = RIGHT
            elif keys[pygame.K_UP]:
                self.pacman.direction = UP
            elif keys[pygame.K_DOWN]:
                self.pacman.direction = DOWN

            self.all_sprites.update()

            self.screen.fill(BLACK)
            self.all_sprites.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
