import pygame
import sys
from game.board import Board
from agents.human_agent import HumanAgent
from agents.random_agent import RandomAgent
from ui.pygame_draw import draw_board

# Pygame init
pygame.init()

# Constantes
ROWS = 7
COLS = 7
SQUARESIZE = 100
WIDTH = COLS * SQUARESIZE
HEIGHT = (ROWS + 1) * SQUARESIZE
SIZE = (WIDTH, HEIGHT)

WHITE = (255, 255, 255)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Connect 4")

font = pygame.font.SysFont("monospace", 75)

def play_game(player1, player2):
    board = Board(ROWS, COLS)
    current_player = player1
    draw_board(screen, board.grid)
    game_over = False

    while not game_over:
        pygame.time.wait(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        col = current_player.get_move(board) 

        if col is not None and board.is_valid_move(col):
            row = board.get_next_open_row(col)
            board.drop_piece(row, col, current_player.symbol)
            draw_board(screen, board.grid)

            if board.check_win(current_player.symbol):
                label = font.render(f"{current_player.symbol} wins!", True, WHITE)
                screen.blit(label, (40, 10))
                pygame.display.update()
                pygame.time.wait(3000)
                game_over = True
            elif board.is_full():
                label = font.render("Draw!", True, WHITE)
                screen.blit(label, (40, 10))
                pygame.display.update()
                pygame.time.wait(3000)
                game_over = True
            else:
                current_player = player2 if current_player == player1 else player1
        elif isinstance(current_player, HumanAgent):
            pygame.time.wait(1000)

if __name__ == "__main__":
    # p1 = HumanAgent("X", screen, SQUARESIZE) 
    p1 = RandomAgent("X")
    p2 = RandomAgent("O")
    play_game(p1, p2)
