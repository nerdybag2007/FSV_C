def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("---------")
    print("\n")

def check_winner(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(board[r][i] == player for r in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_move(player):
    while True:
        try:
            move = input(f"Player {player}, enter row and column (1-3 separated by space): ").split()
            if len(move) != 2:
                raise ValueError
            row, col = int(move[0]) - 1, int(move[1]) - 1
            if row not in range(3) or col not in range(3):
                raise ValueError
            return row, col
        except ValueError:
            print("Invalid input. Please enter two numbers between 1 and 3.")

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row, col = get_move(current_player)

        if board[row][col] != " ":
            print("That cell is already taken. Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
