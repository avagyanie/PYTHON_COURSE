import random

class Board:
    def __init__(self):
        self.board = [" " for elem in range(9)]
        self.current_player = "X"

    def print_board(self):
        print("-------------")
        for i in range(3):
            print("|", self.board[i * 3], "|", self.board[i * 3 + 1], "|", self.board[i * 3 + 2], "|")
            print("-------------")

    def make_move(self, position):
        self.board[position] = self.current_player

    def is_valid_move(self, position):
        return self.board[position] == " "

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def check_win(self, player):
        # check rows
        for j in range(0, 9, 3):
            if self.board[j] == self.board[j + 1] == self.board[j + 2] == player:
                return True

        # check columns
        for m in range(3):
            if self.board[m] == self.board[m + 3] == self.board[m + 6] == player:
                return True

        # check diagonals
        if self.board[0] == self.board[4] == self.board[8] == player:
            return True
        if self.board[2] == self.board[4] == self.board[6] == player:
            return True

        return False

    def check_draw(self):
        return " " not in self.board

class Player:
    def __init__(self, player_symbol):
        self.player_symbol = player_symbol

class HumanPlayer(Player):
    def __init__(self, player_symbol):
        super().__init__(player_symbol)

    def get_move(self):
        while True:
            try:
                position = int(input("Enter position (1-9): ")) - 1
                if 0 <= position <= 8:
                    return position
                else:
                    print("Invalid position. Please, try again.")
            except ValueError:
                print("Invalid symbol. Please, enter a number.")

class ComputerPlayer(Player):
    def __init__(self, player_symbol):
        super().__init__(player_symbol)

    def get_move(self, board):
        available_moves = [k for k in range(9) if board.is_valid_move(k)]
        return random.choice(available_moves)

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
