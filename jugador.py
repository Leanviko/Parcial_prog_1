import pygame
import math

class Jugador:
    def __init__(self,a_game):
        
        self.pantalla = a_game.pantalla
        self.pantalla_rect = a_game.pantalla.get_rect()
        self.image = pygame.image.load("Images/Jugador/survivor-move_rifle_0.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.pantalla_rect.midbottom
        
        self.mover_derecha = False
        self.mover_izquierda = False
        self.mover_arriba = False
        self.mover_abajo = False
    
    def mover(self):
        if self.mover_derecha and self.rect.right < self.pantalla_rect.right:
            self.rect.x += 1
        if self.mover_izquierda and self.rect.left > 0:
            self.rect.x -= 1
        if self.mover_arriba and self.rect.top > 0:
            self.rect.y -= 1
        if self.mover_abajo and self.rect.bottom < self.pantalla_rect.bottom:
            self.rect.y += 1
        
        posicion_mouse = pygame.mouse.get_pos()
        x_distancia = posicion_mouse[0] - self.rect.center[0]-1
        y_distancia = posicion_mouse[1] - self.rect.center[1]
        grados = math.degrees(math.atan2(x_distancia, y_distancia))
        self.imagen_rotacion = pygame.transform.rotate(self.image,grados-90)
        
    
    def dibujar(self):
        self.pantalla.blit(self.imagen_rotacion,self.rect)