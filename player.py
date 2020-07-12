import pygame

rojo = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
negro = (0,0,0)
blanco = (255,255,255)

class Player():
    def __init__(self, x, y, pantalla):
        self.x = x
        self.y = y

        self.derecha = False
        self.izquierda = False
        self.arriba = False
        self.abajo = False
        self.color = blanco
        self.image = pygame.image.load('player_sprite.png')
        self.rect = pygame.Rect(self.x,self.y,64,64)

        self.walkCount = 0
        sprite_size = 64
        rows = 4
        columns = 9
        self.sprites = [[0 for x in range(columns)] for y in range(rows)] 

        for row in range(rows):
            for column in range(columns):
                image = pygame.Surface([sprite_size,sprite_size])
                image.blit(self.image, (0, 0), (column * sprite_size, row * sprite_size, sprite_size, sprite_size))
                image.set_colorkey((0,255,0))
                self.sprites[row][column] = image 

        self.move_left = [0 for y in range(columns)]
        self.move_right = [0 for y in range(columns)] 
        self.move_up = [0 for y in range(columns)]
        self.move_down = [0 for y in range(columns)]

        for column in range(columns):
            self.move_up[column] = self.sprites[0][column]
            self.move_left[column] = self.sprites[1][column]
            self.move_down[column] = self.sprites[2][column]
            self.move_right[column] = self.sprites[3][column]

    def draw(self, pantalla):

        pygame.draw.rect(pantalla, (0,255,0), self.rect)
        if self.walkCount + 1 >= 9:
            self.walkCount = 0

        if self.izquierda:
            pantalla.blit(self.move_left[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        elif self.derecha:
            pantalla.blit(self.move_right[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        elif self.arriba:
            pantalla.blit(self.move_up[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        elif self.abajo:
            pantalla.blit(self.move_down[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        else:
            pantalla.blit(self.sprites[2][0],(self.x, self.y))
            self.walkCount = 0


