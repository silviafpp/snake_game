import pygame

# Tamanho de cada bloco
TILE_SIZE = 20

class Snake:
    # Construtor
    def __init__(self):
        self.body = [(5, 5), (4, 5), (3, 5)]
        self.direction = (1, 0)
        self.grow = False
        self.load_images()
        
    def load_images(self):
        # Dicionário de imagens da cobra (nomes padronizados em minúsculas)
        self.images = {
            "head_up": pygame.transform.scale(pygame.image.load("assets/head_up.png").convert_alpha(), (TILE_SIZE, TILE_SIZE)),
            "head_down": pygame.transform.scale(pygame.image.load("assets/head_down.png").convert_alpha(), (TILE_SIZE, TILE_SIZE)),
            "head_left": pygame.transform.scale(pygame.image.load("assets/head_left.png").convert_alpha(), (TILE_SIZE, TILE_SIZE)),
            "head_right": pygame.transform.scale(pygame.image.load("assets/head_right.png").convert_alpha(), (TILE_SIZE, TILE_SIZE)),
            "body": pygame.transform.scale(pygame.image.load("assets/body.png").convert_alpha(), (TILE_SIZE, TILE_SIZE)),
            "tail_up": pygame.transform.scale(pygame.image.load("assets/tail_up.png").convert_alpha(), (TILE_SIZE, TILE_SIZE)),
            "tail_down": pygame.transform.scale(pygame.image.load("assets/tail_down.png").convert_alpha(), (TILE_SIZE, TILE_SIZE)),
            "tail_left": pygame.transform.scale(pygame.image.load("assets/tail_left.png").convert_alpha(), (TILE_SIZE, TILE_SIZE)),
            "tail_right": pygame.transform.scale(pygame.image.load("assets/tail_right.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
        }
        
    def move(self):
        # Calcula a nova posição da cabeça com base na direção atual
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
    
    def change_direction(self, new_dir):
        # Impede a cobra de virar 180° imediatamente
        opposite = (-self.direction[0], -self.direction[1])
        if new_dir != opposite:
            self.direction = new_dir
            
    def get_head_image(self):
        # Retorna a imagem da cabeça conforme a direção atual
        if self.direction == (0, -1):
            return self.images["head_up"]
        elif self.direction == (0, 1):
            return self.images["head_down"]
        elif self.direction == (-1, 0):
            return self.images["head_left"]
        elif self.direction == (1, 0):
            return self.images["head_right"]
    
    def get_tail_image(self):
        # Determina a orientação da cauda
        if len(self.body) < 2:
            return self.images["tail_right"]
        tail = self.body[-1]
        before_tail = self.body[-2]
        dx = tail[0] - before_tail[0]
        dy = tail[1] - before_tail[1]
        if dx == 1:
            return self.images["tail_left"]
        elif dx == -1:
            return self.images["tail_right"]
        elif dy == 1:
            return self.images["tail_up"]
        elif dy == -1:
            return self.images["tail_down"]
        return self.images["tail_right"]
    
    def draw(self, screen):
        for i, (x, y) in enumerate(self.body):
            pos = (x * TILE_SIZE, y * TILE_SIZE)
            if i == 0:
                image = self.get_head_image()
            elif i == len(self.body) - 1:
                image = self.get_tail_image()
            else:
                image = self.images["body"]
            screen.blit(image, pos)
    
    def check_collision(self, width, height):
        # Detecta colisões com paredes ou com o próprio corpo
        head = self.body[0]
        if not (0 <= head[0] < width // TILE_SIZE and 0 <= head[1] < height // TILE_SIZE):
            return True
        if head in self.body[1:]:
            return True
        return False
