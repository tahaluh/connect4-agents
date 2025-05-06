import pygame

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

def draw_board(screen, grid, top_left=(0, 100), square_size=100):
    """
    Desenha o tabuleiro do Connect 4 com base no grid atual, a partir de uma posição inicial.

    :param screen: superfície pygame
    :param grid: matriz 2D com " ", "X" ou "O"
    :param top_left: tupla (x, y) da posição inicial do canto superior esquerdo
    :param square_size: tamanho de cada célula do tabuleiro
    """
    offset_x, offset_y = top_left
    rows = len(grid)
    cols = len(grid[0])
    radius = square_size // 2 - 5

    for r in range(rows):
        for c in range(cols):
            # Desenha fundo azul + buraco preto
            pygame.draw.rect(
                screen,
                BLUE,
                (
                    offset_x + c * square_size,
                    offset_y + r * square_size,
                    square_size,
                    square_size
                )
            )
            pygame.draw.circle(
                screen,
                BLACK,
                (
                    offset_x + c * square_size + square_size // 2,
                    offset_y + r * square_size + square_size // 2
                ),
                radius
            )

    # Desenha peças (de baixo pra cima)
    for r in range(rows):
        for c in range(cols):
            piece = grid[r][c]
            x = offset_x + c * square_size + square_size // 2
            y = offset_y + r * square_size + square_size // 2

            if piece == "X":
                pygame.draw.circle(screen, RED, (x, y), radius)
            elif piece == "O":
                pygame.draw.circle(screen, YELLOW, (x, y), radius)

    pygame.display.update()
