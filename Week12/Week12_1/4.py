board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'


def draw_board():
    # drow a board
    print('_______')
    for row in board:
        print('|', end='')
        for cell in row:
            print(cell, end='|')
        print('\n_______')

def get_move():
    while True:
        try:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Try again.")


def make_move(row, col, player):
    board[row][col] = player


def check_winner():
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False


def check_tie():
    for row in board:
        if ' ' in row:
            return False
    return True


def reset_game():
    global board, current_player
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'


# Main game loop
while True:
    draw_board()
    print(f"Player {current_player}'s turn.")
    move = get_move()
    make_move(move[0], move[1], current_player)
    if check_winner():
        draw_board()
        print(f"Player {current_player} wins!")
        reset_game()
    elif check_tie():
        draw_board()
        print("It's a tie!")
        reset_game()
    else:
        current_player = 'O' if current_player == 'X' else 'X'
        