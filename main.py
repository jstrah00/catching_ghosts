import pygame
from pygame.locals import *
from player import *

pygame.init()

ancho_pantalla = 600
alto_pantalla = 600
FPS = 20

pantalla = pygame.display.set_mode([ancho_pantalla, alto_pantalla])
fondo = pygame.image.load('fondo.jpg')
reloj = pygame.time.Clock()

run = True
x = 0
y = 0

def actualizar_pantalla():
    jugador.draw(pantalla)
    pygame.display.update()

    pantalla.blit(fondo,(x,y))
jugador = Player(alto_pantalla/2, ancho_pantalla/2)

while run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            exit()

    pulsada = pygame.key.get_pressed()
 
    if pulsada[K_LEFT]:
        x += 5
    if pulsada[K_RIGHT]:
        x -= 5


    actualizar_pantalla()
    reloj.tick(FPS)


