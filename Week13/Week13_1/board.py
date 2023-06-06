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

if __name__ == "__main__":
    x = Board()
    x.print_board()
