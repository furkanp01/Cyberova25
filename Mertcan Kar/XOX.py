import random


class Board:
    def __init__(self):
        self.board = ["-", "-", "-",
                      "-", "-", "-",
                      "-", "-", "-"]
        self.winner = None

    def print_board(self):
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])

    def update_board(self, position, player):
        self.board[position] = player

    def check_row(self):
        if self.board[0] == self.board[1] == self.board[2] and self.board[0] != "-":
            self.winner = self.board[0]
            return True
        elif self.board[3] == self.board[4] == self.board[5] and self.board[3] != "-":
            self.winner = self.board[3]
            return True
        elif self.board[6] == self.board[7] == self.board[8] and self.board[6] != "-":
            self.winner = self.board[6]
            return True
        return False

    def check_col(self):
        if self.board[0] == self.board[3] == self.board[6] and self.board[0] != "-":
            self.winner = self.board[0]
            return True
        elif self.board[1] == self.board[4] == self.board[7] and self.board[1] != "-":
            self.winner = self.board[1]
            return True
        elif self.board[2] == self.board[5] == self.board[8] and self.board[2] != "-":
            self.winner = self.board[2]
            return True
        return False

    def check_diagonal(self):
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] != "-":
            self.winner = self.board[0]
            return True
        elif self.board[2] == self.board[4] == self.board[6] and self.board[2] != "-":
            self.winner = self.board[2]
            return True
        return False

    def check_win(self):
        if self.check_row() or self.check_col() or self.check_diagonal():
            return True
        return False

    def check_tie(self):
        if "-" not in self.board:
            return True
        return False


class Main:
    def __init__(self):
        self.board = Board()
        self.current_player = "X"
        self.is_game_running = True

    def player_input(self):
        while True:
            try:
                inp = int(input("1 ile 9 arası bir sayı giriniz: "))
                if inp < 1 or inp > 9:
                    print("Lütfen 1 ile 9 arasında bir sayı giriniz.")
                elif self.board.board[inp - 1] != "-":
                    print("Burası dolu, başka bir sayı giriniz.")
                else:
                    self.board.update_board(inp - 1, self.current_player)
                    break
            except ValueError:
                print("Lütfen bir sayı giriniz.")

    def comp(self):
        while self.current_player == "0":
            position = random.randint(0, 8)
            if self.board.board[position] == "-":
                self.board.update_board(position, "0")
                break

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "0"
        else:
            self.current_player = "X"

    def play(self):
        while self.is_game_running:
            self.board.print_board()
            if self.current_player == "X":
                self.player_input()
            else:
                self.comp()

            if self.board.check_win():
                self.board.print_board()
                print(f"{self.board.winner} kazandı!")
                self.is_game_running = False
            elif self.board.check_tie():
                self.board.print_board()
                print("Beraberlik!")
                self.is_game_running = False
            else:
                self.switch_player()


main = Main()
main.play()
