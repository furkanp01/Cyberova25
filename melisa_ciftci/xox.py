class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.game_on = True

    def print_board(self):
        print()
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("--------------")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("--------------")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

    def check_win(self, player):
        win_combos = [
            [0,1,2], [3,4,5],[6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        for combo in win_combos:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def check_draw(self):
        return " " not in self.board

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def make_move(self):
        try:
            move = int(input("1-9 arasında bir hamle seç: ")) - 1
            if move < 0 or move > 8:
                print("Geçersiz hamle!")
                return False
            if self.board[move] != " ":
                print("Kare dolu, başka bir yer seç.")
                return False
            self.board[move] = self.current_player
            return True
        except ValueError:
            print("Bir sayı girmen gerekiyor.")
            return False

    def play(self):
        while self.game_on:
            self.print_board()
            print(f"Sıra: {self.current_player}")

            if not self.make_move():
                continue

            if self.check_win(self.current_player):
                self.print_board()
                print(f"Oyuncu {self.current_player} kazandı!")
                break

            if self.check_draw():
                self.print_board()
                print("Berabere!")
                break

            self.switch_player()


if __name__ == "__main__":
    game = TicTacToe()
    game.play()