import pygame
import random

# Inicializamos pygame
pygame.init()

# Configuración básica de la pantalla
ANCHO, ALTO = 300, 600
TAMAÑO_CELDA = 30
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Tetris Básico")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
COLORES = [
    (255, 0, 0),  # Rojo
    (0, 255, 0),  # Verde
    (0, 0, 255),  # Azul
    (255, 255, 0),  # Amarillo
    (0, 255, 255),  # Cyan
]

# Formas de las piezas (Tetrominós)
PIEZAS = [
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1], [1, 1]],        # Cuadrado
    [[1, 1, 1, 1]],          # Línea
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # S
]

# Clase para manejar las piezas
class Pieza:
    def __init__(self):
        self.forma = random.choice(PIEZAS)
        self.color = random.choice(COLORES)
        self.x = ANCHO // TAMAÑO_CELDA // 2 - len(self.forma[0]) // 2
        self.y = 0

    def rotar(self):
        # Rotación de la pieza (transposición y reversión)
        self.forma = [list(fila) for fila in zip(*self.forma[::-1])]

# Función para dibujar la cuadrícula
def dibujar_cuadricula():
    for x in range(0, ANCHO, TAMAÑO_CELDA):
        pygame.draw.line(pantalla, BLANCO, (x, 0), (x, ALTO))
    for y in range(0, ALTO, TAMAÑO_CELDA):
        pygame.draw.line(pantalla, BLANCO, (0, y), (ANCHO, y))

# Función para dibujar una pieza
def dibujar_pieza(pieza):
    for i, fila in enumerate(pieza.forma):
        for j, celda in enumerate(fila):
            if celda:
                pygame.draw.rect(
                    pantalla,
                    pieza.color,
                    pygame.Rect(
                        (pieza.x + j) * TAMAÑO_CELDA,
                        (pieza.y + i) * TAMAÑO_CELDA,
                        TAMAÑO_CELDA,
                        TAMAÑO_CELDA,
                    ),
                )

# Función principal del juego
def main():
    reloj = pygame.time.Clock()
    pieza_actual = Pieza()
    tablero = [[0] * (ANCHO // TAMAÑO_CELDA) for _ in range(ALTO // TAMAÑO_CELDA)]

    corriendo = True
    while corriendo:
        pantalla.fill(NEGRO)
        dibujar_cuadricula()
        dibujar_pieza(pieza_actual)

        # Eventos del juego
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    pieza_actual.x -= 1
                elif evento.key == pygame.K_RIGHT:
                    pieza_actual.x += 1
                elif evento.key == pygame.K_DOWN:
                    pieza_actual.y += 1
                elif evento.key == pygame.K_UP:
                    pieza_actual.rotar()

        # Movimiento automático hacia abajo
        pieza_actual.y += 1

        pygame.display.flip()
        reloj.tick(10)  # Controla la velocidad del juego

    pygame.quit()

if __name__ == "__main__":
    main()