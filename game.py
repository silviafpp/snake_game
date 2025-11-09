import pygame
import sys
from snake import Snake
from apple import Apple

WIDTH, HEIGHT = 800, 600
TILE_SIZE = 20
GREEN = (140, 215, 120)
DARK_GREEN = (130, 205, 110)
SCREEN_GREEN = (46, 111, 64)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 25, True)
        self.big_font = pygame.font.SysFont("Arial", 40, True)
        self.reset_game()
        self.high_score = 0
        self.state = "menu"

    def reset_game(self):
        self.snake = Snake()
        self.apple = Apple(WIDTH, HEIGHT)
        self.score = 0
        self.running = True

    def draw_grid(self):
        for y in range(0, HEIGHT, TILE_SIZE):
            for x in range(0, WIDTH, TILE_SIZE):
                rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                color = GREEN if (x // TILE_SIZE + y // TILE_SIZE) % 2 == 0 else DARK_GREEN
                pygame.draw.rect(self.screen, color, rect)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction((1, 0))

    def update(self):
        self.snake.move()
        if self.snake.body[0] == self.apple.position:
            self.score += 1
            self.snake.grow = True
            self.apple = Apple(WIDTH, HEIGHT)
        if self.snake.check_collision(WIDTH, HEIGHT):
            if self.score > self.high_score:
                self.high_score = self.score
            self.state = "game_over"

    def draw_playing(self):
        self.draw_grid()
        self.apple.draw(self.screen)
        self.snake.draw(self.screen)

        text = self.font.render(f"Maçãs: {self.score}", True, BLACK)
        self.screen.blit(text, (10, 10))

        high_text = self.font.render(f"Recorde: {self.high_score}", True, BLACK)
        self.screen.blit(high_text, (WIDTH - high_text.get_width() - 10, 10))

        pygame.display.flip()

    def menu_screen(self):
        while self.state == "menu":
            self.screen.fill(SCREEN_GREEN)
            title = self.big_font.render("Bem-vindo/a ao Snake Game!", True, WHITE)
            play_text = self.font.render("Jogar (ENTER)", True, WHITE)
            exit_text = self.font.render("Sair (ESC)", True, WHITE)

            self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
            self.screen.blit(play_text, (WIDTH // 2 - play_text.get_width() // 2, HEIGHT // 2))
            self.screen.blit(exit_text, (WIDTH // 2 - exit_text.get_width() // 2, HEIGHT // 2 + 40))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.state = "playing"
                        self.reset_game()
                        return
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

    def game_over_screen(self):
        while self.state == "game_over":
            self.screen.fill(SCREEN_GREEN)
            over_text = self.big_font.render("Game Over!", True, WHITE)
            score_text = self.font.render(f"Maçãs comidas: {self.score}", True, WHITE)
            record_text = self.font.render(f"Recorde: {self.high_score}", True, WHITE)
            restart_text = self.font.render("Recomeçar (R)", True, WHITE)
            exit_text = self.font.render("Sair (ESC)", True, WHITE)

            self.screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 3))
            self.screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - 20))
            self.screen.blit(record_text, (WIDTH // 2 - record_text.get_width() // 2, HEIGHT // 2 + 10))
            self.screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 60))
            self.screen.blit(exit_text, (WIDTH // 2 - exit_text.get_width() // 2, HEIGHT // 2 + 90))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.state = "playing"
                        self.reset_game()
                        return
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

    def run(self):
        while True:
            if self.state == "menu":
                self.menu_screen()
            elif self.state == "playing":
                self.clock.tick(10)
                self.handle_input()
                self.update()
                self.draw_playing()
            elif self.state == "game_over":
                self.game_over_screen()