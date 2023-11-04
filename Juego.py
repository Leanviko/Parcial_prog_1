import pygame
import sys
from jugador import Jugador

class Juego_soldado:
    def __init__(self):
        pygame.init()
        PANTALLA_ANCHO = 1024
        PANTALLA_ALTO = 768
        self.pantalla = pygame.display.set_mode((PANTALLA_ANCHO,PANTALLA_ALTO))
        pygame.display.set_caption('Juego')
        self.color = (200,200,100)
        self.jugador = Jugador(self)

    def corriendo_juego(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_a: 
                        self.jugador.mover_izquierda = True
                    if evento.key == pygame.K_d:
                        self.jugador.mover_derecha = True
                    if evento.key == pygame.K_w:
                        self.jugador.mover_arriba = True
                    if evento.key == pygame.K_s:
                        self.jugador.mover_abajo = True
                    

                elif evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_a: 
                        self.jugador.mover_izquierda = False
                    if evento.key == pygame.K_d:
                        self.jugador.mover_derecha = False
                    if evento.key == pygame.K_w:
                        self.jugador.mover_arriba = False
                    if evento.key == pygame.K_s:
                        self.jugador.mover_abajo = False
            
            self.jugador.mover()
            self.pantalla.fill(self.color)
            self.jugador.dibujar()
            pygame.display.flip()

if __name__ == '__main__':
    a = Juego_soldado()
    a.corriendo_juego()