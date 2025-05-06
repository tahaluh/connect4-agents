ROWS = 7
COLS = 7

class Board:
    def __init__(self, rows=ROWS, cols=COLS):
        self.grid = [[" " for _ in range(cols)] for _ in range(rows)]
        self.rows = rows
        self.cols = cols

    def print(self):
        for row in self.grid:
            print("|" + "|".join(row) + "|")
        print(" " + " ".join(str(i) for i in range(self.cols)))

    def is_valid_move(self, col):
        return 0 <= col < self.cols and self.grid[0][col] == " "

    def get_next_open_row(self, col):
        for row in range(self.rows - 1, -1, -1):
            if self.grid[row][col] == " ":
                return row
        return None

    def drop_piece(self, row, col, player):
        self.grid[row][col] = player

    def check_win(self, player):
        # Check horizontal
        for r in range(self.rows):
            for c in range(self.cols - 3):
                if all(self.grid[r][c + i] == player for i in range(4)):
                    return True

        # Check vertical
        for c in range(self.cols):
            for r in range(self.rows - 3):
                if all(self.grid[r + i][c] == player for i in range(4)):
                    return True

        # Check diagonal (positive slope) /
        for r in range(3, self.rows):
            for c in range(self.cols - 3):
                if all(self.grid[r - i][c + i] == player for i in range(4)):
                    return True

        # Check diagonal (negative slope) \
        for r in range(self.rows - 3):
            for c in range(self.cols - 3):
                if all(self.grid[r + i][c + i] == player for i in range(4)):
                    return True

        return False

    def is_full(self):
        return all(self.grid[0][c] != " " for c in range(self.cols))
