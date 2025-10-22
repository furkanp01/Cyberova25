class xoxo:
    def __init__(self):
        self.board = ['-', '-', '-',
                 '-', '-', '-',
                 '-', '-', '-']
    def display(self):
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]} \n"
              f"{self.board[3]} | {self.board[4]} | {self.board[5]} \n"
              f"{self.board[6]} | {self.board[7]} | {self.board[8]}")


    def is_valid(self,position):
        if not (1<= position<=9):
            return False, "Hatalı sayı girildi"
        if self.board[position-1] == "-":
            return True, ""
        else:
            return False,

    def make_move(self,position,player_mark):
        self.board[position-1] =player_mark

    def check_win(self,mark):
        winning_combination = [(0,1,2),(3,4,5),(6,7,8),
                               (0,3,6),(1,4,7),(2,5,8),
                               (0,4,8),(2,4,6)]
        for combo in winning_combination:
            if all(self.board[i] == mark for i in combo):
                return True
        return False
    def is_draw(self):
        return '-' not in self.board


class Game:
    def __init__(self):
        self.Board =xoxo()
        self.current_player ='x'
        self.game_on = True
    def switch_player(self):
        if self.current_player=="x":
            self.current_player ="o"
        elif self.current_player=="o":
            self.current_player= "x"
    def get_player_move(self):
        while True:
            try:
                prompt = f"Oyuncu {self.current_player},hamle (1-9)"
                position = int(input(prompt))

                is_valid,message =self.Board.is_valid(position)

                if is_valid:
                    return position
                else:
                    print(message)

            except ValueError:
                print("value error")

    def play(self):
        while self.game_on == True:
            self.Board.display()
            print(f"Sıra: Oyuncu {self.current_player}")
            move =self.get_player_move()

            self.Board.make_move(move,self.current_player)

            if (self.Board.check_win(self.current_player)):
                self.Board.display()
                print(f"{self.current_player} Kazandı")
                self.game_on =False
                continue

            if self.Board.is_draw()== True:
                self.Board.display()
                print("Oyun berabere")
                self.game_on = False
                continue

            self.switch_player()

if __name__ == "__main__":
    game= Game()
    game.play()

