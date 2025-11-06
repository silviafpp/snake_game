import pygame
import random

TILE_SIZE = 20

class Apple:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = pygame.image.load("assets/apple.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.position = self.random_position()

    def random_position(self):
        return (
            random.randint(0, self.width // TILE_SIZE - 1),
            random.randint(0, self.height // TILE_SIZE - 1)
        )

    def draw(self, screen):
        x, y = self.position
        screen.blit(self.image, (x * TILE_SIZE, y * TILE_SIZE))