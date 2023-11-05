import pygame
import math

class Jugador:
    def __init__(self,a_game):
        
        self.pantalla = a_game.pantalla
        self.pantalla_rect = a_game.pantalla.get_rect()
        self.image = pygame.image.load("Images/escudo.png").convert_alpha()
        self.image_personaje = pygame.image.load("Images/Jugador/survivor-move_rifle_0.png").convert_alpha()
        
        self.rect = self.image.get_rect()
        self.personaje_rect = self.image_personaje.get_rect()
        self.rect.midbottom = self.pantalla_rect.midbottom
        self.personaje_rect.centerx = self.rect.centerx
        self.personaje_rect.centery = self.rect.centery

        
        
        
        self.mover_derecha = False
        self.mover_izquierda = False
        self.mover_arriba = False
        self.mover_abajo = False
    
    def mover(self):
        if self.mover_derecha and self.rect.right < self.pantalla_rect.right:
            self.rect.centerx += 1
        if self.mover_izquierda and self.rect.left > 0:
            self.rect.centerx -= 1
        if self.mover_arriba and self.rect.top > 0:
            self.rect.centery -= 1
        if self.mover_abajo and self.rect.bottom < self.pantalla_rect.bottom:
            self.rect.centery += 1
        
        self.personaje_rect.centerx = self.rect.centerx
        self.personaje_rect.centery = self.rect.centery
        

        posicion_mouse = pygame.mouse.get_pos()
        x_distancia = posicion_mouse[0] - self.rect.center[0]
        y_distancia = -(posicion_mouse[1] - self.rect.center[1])
        grados = math.degrees(math.atan2(y_distancia, x_distancia))
        self.imagen_escala = pygame.transform.scale_by(self.image,0.5)

        self.imagen_rotacion = pygame.transform.rotate(self.imagen_escala,grados-90)
        self.rect = self.imagen_rotacion.get_rect(center = (self.rect.center))
        
    
    def dibujar(self):
        self.pantalla.blit(self.imagen_rotacion,self.rect)
        self.pantalla.blit(self.image_personaje,self.personaje_rect)