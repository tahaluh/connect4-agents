import pygame
import sys
from game.board import Board
from agents.random_agent import RandomAgent
from agents.human_agent import HumanAgent
from agents.minmax_agent import MinMaxAgent
from ui.pygame_draw import draw_board

WHITE = (255, 255, 255)
ROWS, COLS = 7, 7

def play_grid_games(grid_size, total_games, screen_size=(1400, 1600)):
    pygame.init()

    grid_rows, grid_cols = grid_size
    max_games = grid_rows * grid_cols
    total_games = min(total_games, max_games)

    screen_width, screen_height = screen_size

    board_pixel_width = screen_width // grid_cols
    board_pixel_height = screen_height // grid_rows
    square_size_x = board_pixel_width // COLS
    square_size_y = board_pixel_height // ROWS
    square_size = min(square_size_x, square_size_y)

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Connect 4 Grid")
    font = pygame.font.SysFont("monospace", square_size // 2)

    games = []
    for i in range(total_games):
        board = Board(ROWS, COLS)
        #player1 = HumanAgent("X", screen, square_size) 
        player1 = RandomAgent("X")
        #player1 = MinMaxAgent("X", depth=1)
        player2 = MinMaxAgent("O", depth=4)
        games.append({
            "board": board,
            "players": [player1, player2],
            "current": 0,
            "over": False,
            "top_left": (
                (i % grid_cols) * board_pixel_width,
                (i // grid_cols) * board_pixel_height
            )
        })

    while not all(g["over"] for g in games):
        #pygame.time.wait(200)

        for g in games:
            if g["over"]:
                continue
            
            board = g["board"]
            draw_board(screen, board.grid, top_left=g["top_left"], square_size=square_size)

            p1, p2 = g["players"]
            current_player = p1 if g["current"] == 0 else p2
            col = current_player.get_move(board)

            if col is not None and board.is_valid_move(col):
                row = board.get_next_open_row(col)
                board.drop_piece(row, col, current_player.symbol)

                if board.check_win(current_player.symbol):
                    draw_board(screen, board.grid, top_left=g["top_left"], square_size=square_size)

                    x, y = g["top_left"]
                    label = font.render(f"{current_player.symbol} wins!", True, WHITE)
                    
                    text_rect = label.get_rect(topleft=(x + 10, y + 10))
                    pygame.draw.rect(screen, (0, 0, 0), text_rect.inflate(20, 10))  
                    screen.blit(label, text_rect.topleft)

                    screen.blit(label, (x + 10, y + 10))
                    pygame.display.update()
                    g["over"] = True
                elif board.is_full():
                    draw_board(screen, board.grid, top_left=g["top_left"], square_size=square_size)
                    
                    x, y = g["top_left"]
                    label = font.render("Draw!", True, WHITE)
                    
                    text_rect = label.get_rect(topleft=(x + 10, y + 10))
                    pygame.draw.rect(screen, (0, 0, 0), text_rect.inflate(20, 10))  
                    screen.blit(label, text_rect.topleft)
                    
                    screen.blit(label, (x + 10, y + 10))
                    pygame.display.update()
                    g["over"] = True
                else:
                    g["current"] = 1 - g["current"]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
    

if __name__ == "__main__":
    play_grid_games(grid_size=(4,4), total_games=16, screen_size=(800, 800))
    pygame.time.wait(3000)
