class Board:
    def __init__(self, width, height):
        self.width = 3
        self.height = 3
        self.board = [[" " for x in range(width)] for y in range(height)]

    def print_board(self):
        print("-------------")
        for row in self.board:
            print("| " + " | ".join(row) + " |")
            print("-------------")

    def reset_board(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def check_win(self,):
        board = self.board
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

    def is_full(self):
        for row in self.board:
            if " " in row:
                return False
        return True

    def place(self, row, col, symbol):

        if self.board[row][col] == " ":
            self.board[row][col] = symbol
            return True
        return False


class XOX:
    def __init__(self):
        self.board = Board(3,3)
        self.current = "X"


    def switch_player(self):
        self.current = "O" if self.current == "X" else "X"


    def parse_input(self, s): # fikir gpt'den alindi
        s = s.replace(",", " ").strip()
        parts = s.split()
        if len(parts) != 2:
            return None
        try:
            r = int(parts[0]) - 1
            c = int(parts[1]) - 1
        except ValueError:
            return None
        if 0 <= r < 3 and 0 <= c < 3:
            return (r, c)
        return None

    def start(self):
        print("Welcome to XOX!!")

        while True:
            self.board.print_board()
            move = input(f"({self.current}) make your move (row column): ").strip()
            if move.lower() in ("q", "quit","exit"):
                print("Thank you for playing")
                break
            parsed_move = self.parse_input(move)
            if not parsed_move:
                print("Invalid input")
                continue
            row, col = parsed_move
            if not self.board.place(row,col, self.current):
                print("Cell is full,try another move")
                continue
            winner = self.board.check_win()
            if winner:
                self.board.print_board()
                print(f"{winner} won")
                break
            if self.board.is_full():
                self.board.print_board()
                print("DRAW!")
                break
            self.switch_player()


if __name__ == "__main__":
    game = XOX()
    game.start()
