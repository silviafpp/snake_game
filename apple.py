import pygame
import random

TILE_SIZE = 20

class Apple:
    # Construtor
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = pygame.image.load("assets/apple.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.position = self.random_position()
        
    def random_position(self):
        # Gera a posição aleatória da maçã
        return(
            random.randint(0, self.width // TILE_SIZE - 1),
            random.randint(0, self.height // TILE_SIZE - 1)
        )
            
    def draw(self, screen):
        # Desenha a maçã
        x, y = self.random_position
        screen.blit(self.image, (x * TILE_SIZE, y * TILE_SIZE))