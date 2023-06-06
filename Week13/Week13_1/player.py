from random import choice
from board import Board


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
        return choice(available_moves)


if __name__ == "__main__":
    x = Player("X")
    y = HumanPlayer("X")
    z = ComputerPlayer("O")
    y.get_move()
    z.get_move(Board)
