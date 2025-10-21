class XOX:
    def __init__(self):
        self.cells = []
        for i in range(1, 10):
            self.cells.append(str(i))

    def print_board(self):

        print()
        print(f" {self.cells[0]} | {self.cells[1]} | {self.cells[2]} ")
        print("-----------")
        print(f" {self.cells[3]} | {self.cells[4]} | {self.cells[5]} ")
        print("-----------")
        print(f" {self.cells[6]} | {self.cells[7]} | {self.cells[8]} ")
        print()

    def update_cell(self, index, mark):

        if self.cells[index] not in ('X', 'O'):
            self.cells[index] = mark
            return True
        else:
            return False

    def check_win(self, mark):

        win_positions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)]

        for a, b, c in win_positions:
            if self.cells[a] == self.cells[b] == self.cells[c] == mark:
                return True
        else:
            return False

    def is_full(self):

        for cell in self.cells:
            if cell not in ('X', 'O'):
                return False
        else:
            return True


class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def make_move(self, board: 'XOX'):

        while True:
            try:
                move = int(input(f"{self.name} ({self.mark}) - hamle yapın (1-9): ")) - 1
                if move < 0 or move > 8:
                    print("Lütfen 1 ile 9 arasında bir sayı giriniz.")
                    continue
                elif not board.update_cell(move, self.mark):
                    print("Burası doluu, başka bir yere oynayın.")
                    continue
                else:
                    break
            except ValueError:
                print("Geçersiz giriş! Sayı girin.")


class Game:
    def __init__(self):
        print("XOX OYUNU")
        name_x = input("X oyuncusunun ismi: ").strip() or "X oyuncusu"
        name_o = input("O oyuncusunun ismi: ").strip() or "O oyuncusu"

        self.board = XOX()
        self.player_x = Player(name_x, 'X')
        self.player_o = Player(name_o, 'O')
        self.current_player = self.player_x

    def switch_player(self):

        if self.current_player == self.player_x:
            self.current_player = self.player_o
        elif self.current_player == self.player_o:
            self.current_player = self.player_x

    def play(self):

        while True:
            self.board.print_board()
            self.current_player.make_move(self.board)

            if self.board.check_win(self.current_player.mark):
                self.board.print_board()
                print("Tebrikler " + self.current_player.name + "! (" + self.current_player.mark + ") kazandı.")

                break
            elif self.board.is_full():
                self.board.print_board()
                print("Berabere! ")
                break
            else:
                self.switch_player()

        self.play_again()

    def play_again(self):

        again = input("Tekrar oynamak ister misiniz ? (e/h): ").strip().lower()
        if again in ('e', 'evet'):
            game = Game()
            game.play()
        elif again in ('h', 'hayır'):
            print("Oyun bitti.")
        else:
            print("Geçersiz giriş! Oyun kapatılıyor .")


if __name__ == '__main__':
    game = Game()
    game.play() 