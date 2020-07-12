import pygame
from pygame.locals import *
from player import *
from map import *

pygame.init()

ancho_pantalla = 600
alto_pantalla = 600
FPS = 27

pantalla = pygame.display.set_mode([ancho_pantalla, alto_pantalla])
fondo = pygame.image.load('fondo.jpg')
reloj = pygame.time.Clock()

run = True
x = 0
y = 0

def actualizar_pantalla(x,y):
    pantalla.fill((0,0,0))
    mapa.draw(pantalla, x, y)
    jugador.draw(pantalla)
    
    pygame.display.update()
    
    #pantalla.blit(fondo,(x,y))



jugador = Player(alto_pantalla/2, ancho_pantalla/2, pantalla)
mapa = Map()
while run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            exit()

    pulsada = pygame.key.get_pressed()
 
    if pulsada[K_LEFT] and not mapa.check_collide(jugador.x -15, jugador.y):
        x += 15
        jugador.derecha = False
        jugador.izquierda = True
        jugador.arriba = False
        jugador.abajo = False
    elif pulsada[K_RIGHT] and not mapa.check_collide(jugador.x +15, jugador.y):
        x -= 15
        jugador.derecha = True 
        jugador.izquierda = False
        jugador.arriba = False
        jugador.abajo = False

    elif pulsada[K_UP] and not mapa.check_collide(jugador.x, jugador.y-15):
        y += 15
        jugador.derecha = False
        jugador.izquierda = False
        jugador.arriba = True
        jugador.abajo = False
    elif pulsada[K_DOWN] and not mapa.check_collide(jugador.x, jugador.y+15):
        y -= 15
        jugador.derecha = False
        jugador.izquierda = False
        jugador.arriba = False
        jugador.abajo = True
    else:
        jugador.derecha = False
        jugador.izquierda = False
        jugador.arriba = False
        jugador.abajo = False 








    actualizar_pantalla(x,y)
    reloj.tick(FPS)


