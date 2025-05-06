import pygame

class HumanAgent:
    def __init__(self, symbol, screen, square_size):
        self.symbol = symbol
        self.screen = screen
        self.square_size = square_size

    def get_move(self, board):
        # Espera até o jogador clicar com o mouse
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = event.pos[0]
                    col = x // self.square_size
                    return col
        return None 
