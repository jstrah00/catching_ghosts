import pygame

class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velx = 0
        self.vely = 0
        self.ancho = 50
        self.alto = 100

    def draw(self, pantalla):
        pygame.draw.rect(pantalla, (255,0,0), (self.x, self.y,self.ancho,self.alto))
