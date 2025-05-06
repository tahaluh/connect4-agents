import random

class MinMaxAgent:
    def __init__(self, symbol, depth=3):
        self.symbol = symbol
        self.depth = depth

    def get_move(self, board):
        _, best_col = self.minimax(board, self.depth, -float('inf'), float('inf'), True)
        # print(f"Best move for {self.symbol}: {best_col} - score: {_}")
        return best_col

    def minimax(self, board, depth, alpha, beta, maximizing_player):
        valid_moves = [c for c in range(board.cols) if board.is_valid_move(c)]
        random.shuffle(valid_moves)

        is_terminal = board.check_win(self.symbol) or board.check_win(self.opponent()) or board.is_full()

        if depth == 0 or is_terminal:
            return self.evaluate(board), None

        if maximizing_player:
            max_eval = -float('inf')
            best_col = random.choice(valid_moves)
            for col in valid_moves:
                row = board.get_next_open_row(col)
                temp_board = board.copy()
                temp_board.drop_piece(row, col, self.symbol)
                eval_score, _ = self.minimax(temp_board, depth - 1, alpha, beta, False)
                if eval_score > max_eval:
                    max_eval = eval_score
                    best_col = col
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
            return max_eval, best_col
        else:
            min_eval = float('inf')
            best_col = random.choice(valid_moves)
            for col in valid_moves:
                row = board.get_next_open_row(col)
                temp_board = board.copy()
                temp_board.drop_piece(row, col, self.opponent())
                eval_score, _ = self.minimax(temp_board, depth - 1, alpha, beta, True)
                if eval_score < min_eval:
                    min_eval = eval_score
                    best_col = col
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
            return min_eval, best_col
    
    def evaluate(self, board):
        if board.check_win(self.symbol):
            return 1000
        if board.check_win(self.opponent()):
            return -1000

        return (
            self.count_threes(board, self.symbol) * 1 -
            self.count_threes(board, self.opponent()) * 1
        )

    def opponent(self):
        return "O" if self.symbol == "X" else "X"

    def count_threes(self, board, player):
        count = 0
        for r in range(board.rows):
            for c in range(board.cols - 3):
                window = [board.grid[r][c + i] for i in range(4)]
                if window.count(player) == 3 and window.count(" ") == 1:
                    count += 1

        for c in range(board.cols):
            for r in range(board.rows - 3):
                window = [board.grid[r + i][c] for i in range(4)]
                if window.count(player) == 3 and window.count(" ") == 1:
                    count += 1

        for r in range(board.rows - 3):
            for c in range(board.cols - 3):
                window = [board.grid[r + i][c + i] for i in range(4)]
                if window.count(player) == 3 and window.count(" ") == 1:
                    count += 1

        for r in range(3, board.rows):
            for c in range(board.cols - 3):
                window = [board.grid[r - i][c + i] for i in range(4)]
                if window.count(player) == 3 and window.count(" ") == 1:
                    count += 1

        return count
