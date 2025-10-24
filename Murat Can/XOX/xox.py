def print_board(board):
    print("-------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")



counter = 0
def ask_for_move(board, current_player):
    while True:
        try:
            int_row = int(input("row?(0-2): "))
            if int_row < 0 or int_row > 2:
                print("Please enter a valid row number")
                continue

            int_col = int(input("column?(0-2): "))
            if int_col < 0 or int_col > 2:
                print("Please enter a valid column number")
                continue

            if board[int_row][int_col] != " ":
                print("Cell is full")
                continue

            
            board[int_row][int_col] = current_player
            print_board(board)
            break
        except ValueError:
            print("Please enter a number")


def check_winner(board):

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]


    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]


    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]



    return None



board = [[" " for _ in range(3)] for _ in range(3)]
print_board(board)
current_player = "X"
while True:
    ask_for_move(board, current_player)
    winner = check_winner(board)

    if winner:
        print(f"The winner is {winner}")
        break

    if all(cell != " " for row in board for cell in row):
        print("Berabere!")
        break

    # Oyuncu değişimi
    current_player = "O" if current_player == "X" else "X"






