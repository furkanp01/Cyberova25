class Game:
    def __init__(self,players):
        self.players = players
        self.board = [" "]*9

    def print_board(self):
        print(f" {self.board[0]} {self.board[1]} {self.board[2]} \n",
              f"{self.board[3]} {self.board[4]} {self.board[5]} \n",
              f"{self.board[6]} {self.board[7]} {self.board[8]} \n")

    def get_input(self,player):
        while True:
            i = input(f"{player} starting from 0 <row>,<column>: ")

            if "," not in i:
                print("ERROR: Use row,column format")
                continue

            parts = i.split(",")
            if len(parts) != 2:
                print("ERROR: Enter exactly two numbers separated by a comma")
                continue

            row_str, col_str = parts

            if not (row_str.isdigit() and col_str.isdigit()):
                print("ERROR: Row and column must be numbers")
                continue

            row, column = int(row_str), int(col_str)

            if not (0 <= row <= 2 and 0 <= column <= 2):
                print("ERROR: Row and column must be between 0 and 2")
                continue

            if self.board[3 * row + column] != " ":
                print("Occupied location!")
                continue

            self.board[3 * row + column] = player
            break

    def check_winner(self):
        wins = [
            (0, 1, 2),  # row 1
            (3, 4, 5),  # row 2
            (6, 7, 8),  # row 3
            (0, 3, 6),  # col 1
            (1, 4, 7),  # col 2
            (2, 5, 8),  # col 3
            (0, 4, 8),  # left diagonal
            (2, 4, 6),  # right diagonal
        ]
        for a, b, c in wins:
            if self.board[a] != " " and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        return None

    def check_stalemate(self):
        if len(set(self.board))==1:
            return True
        return False




if __name__ == "__main__":
    print("enter the names, only the first char is valid")
    player_a = input("player a: ")[0]
    player_b = input("player b: ")[0] #doesnt check if both players have conflicting chars first
    game = Game([player_a,player_b])

    while True:
        game.get_input(player_a)
        game.print_board()

        win = game.check_winner()
        if win is not None:
            print(f"{win} wins!")
            break

        game.get_input(player_b)
        game.print_board()

        win = game.check_winner()
        if win is not None:
            print(f"{win} wins!")
            break

        if game.check_stalemate():
            print(f"stalemate!")
            break