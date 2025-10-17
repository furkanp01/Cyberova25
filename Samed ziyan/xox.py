import sys

WIN_COMBOS = [
    (0,1,2), (3,4,5), (6,7,8),  
    (0,3,6), (1,4,7), (2,5,8), 
    (0,4,8), (2,4,6)            
]

def print_board(board):
    def cell(i):
        return board[i] if board[i] != ' ' else str(i+1)
    print(f" {cell(0)} | {cell(1)} | {cell(2)} ")
    print("---+---+---")
    print(f" {cell(3)} | {cell(4)} | {cell(5)} ")
    print("---+---+---")
    print(f" {cell(6)} | {cell(7)} | {cell(8)} ")

def check_win(board, mark):
    return any(board[a]==board[b]==board[c]==mark for a,b,c in WIN_COMBOS)

def is_draw(board):
    return all(cell != ' ' for cell in board)

def get_move(board, player):
    while True:
        try:
            move = input(f"Player {player}, enter your move (1-9): ").strip()
            if move.lower() in ('q','exit'):
                print("Game terminated.")
                sys.exit(0)
            pos = int(move) - 1
            if pos < 0 or pos > 8:
                print("Enter a number between 1 and 9.")
                continue
            if board[pos] != ' ':
                print("That cell is occupied, choose another one.")
                continue
            return pos
        except ValueError:
            print("Invalid input. Try again.")

def main():
    print("Simple Tic-Tac-Toe. Type 'q' or 'exit' to quit.")
    while True:
        board = [' '] * 9
        current = 'X'
        while True:
            print_board(board)
            pos = get_move(board, current)
            board[pos] = current
            if check_win(board, current):
                print_board(board)
                print(f"Player {current} wins!")
                break
            if is_draw(board):
                print_board(board)
                print("It's a draw.")
                break
            current = 'O' if current == 'X' else 'X'
        again = input("Play again? (y/n): ").strip().lower()
        if not again or again[0] != 'y':
            print("Goodbye.")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame terminated.")