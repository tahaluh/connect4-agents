import random

class RandomAgent:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        valid_moves = [c for c in range(7) if board.is_valid_move(c)]
        return random.choice(valid_moves)
