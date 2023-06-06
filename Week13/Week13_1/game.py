from board import Board
from player import Player, HumanPlayer, ComputerPlayer



class TicTacToeGame:
    def __init__(self):
        self.board = Board()
        self.human_player = HumanPlayer("X")
        self.computer_player = ComputerPlayer("O")

    def play_game(self):
        while True:
            self.board.print_board()

            if self.board.current_player == self.human_player.player_symbol:
                position = self.human_player.get_move()
            else:
                position = self.computer_player.get_move(self.board)

            if self.board.is_valid_move(position):
                self.board.make_move(position)

                if self.board.check_win(self.board.current_player):
                    self.board.print_board()
                    print(f"Player {self.board.current_player} wins!")
                    break

                if self.board.check_draw():
                    self.board.print_board()
                    print("It's a draw!")
                    break

                self.board.switch_player()
            else:
                print("Invalid move. Please try again.")


# start the game
if __name__ == "__main__":
    game = TicTacToeGame()
    game.play_game()
