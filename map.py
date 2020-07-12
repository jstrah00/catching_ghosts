import pygame

class Map():
    def __init__(self):
        self.map = [
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '1', '1', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '1', '1', '0', '1', '1', '1', '0'],
        ['0', '0', '0', '1', '1', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
        ]
        self.tile_size = 64
        self.tile_rects = []

    def draw(self, pantalla, x, y):
        count_fila = 0
        self.tile_rects = []
        for fila in self.map:
            count_column = 0
            for tile in fila:
                if tile == '1':
                    color = (255,0,0)
                else:
                    color = (0,0,255)
                my_rect = pygame.Rect(x + self.tile_size * count_column, y + self.tile_size * count_fila, self.tile_size,self.tile_size)
                pygame.draw.rect(pantalla, color, my_rect)

                if tile != '0':
                    self.tile_rects.append(my_rect)

                count_column += 1
            count_fila += 1

    def check_collide(self,x,y):
        rect = pygame.Rect(x,y,64,64)
        for tile in self.tile_rects:
            if rect.colliderect(tile):
                return True

        return False
