from game.board import Board

class Connect4Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.current_player = self.player1

    def switch_player(self):
        self.current_player = (
            self.player1 if self.current_player == self.player2 else self.player2
        )

    def play(self):
        while True:
            self.board.print()
            col = self.current_player.get_move(self.board)
            if self.board.is_valid_move(col):
                row = self.board.get_next_open_row(col)
                self.board.drop_piece(row, col, self.current_player.symbol)
                if self.board.check_win(self.current_player.symbol):
                    self.board.print()
                    print(f"Player {self.current_player.symbol} wins!")
                    break
                elif self.board.is_full():
                    self.board.print()
                    print("It's a tie!")
                    break
                self.switch_player()
            else:
                print("Invalid move. Try again.")
