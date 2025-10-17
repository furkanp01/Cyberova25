class Board:
    def __init__(self):
        self.grid = [
            [" "," "," "],
            [" "," "," "],
            [" "," "," "]
        ]

    def display(self):
        print("\n")
        for i in range(3):
            print(" "+"  |  ".join(self.grid[i]) + " ")

            if i < 2:
                print("----+----+----")


    def hamleYap1(self,row,column,symbol):
        # self.row = row
        # self.column = column
        # self.symbol = symbol 

        if(self.grid[row][column] == " "):
            # print("Lütfen hamle yapiniz(X or O): ")
            self.grid[row][column] = symbol
            return True
        else:   
            return False
        # try:
        #     if(self.grid[row][column] == " "):
        #         self.grid[row][column] = symbol
        #         print("Yerlestirme basarili.")
        # except:
        #     print("Bu hücre dolu")
                    

    def beraberlik(self):
        for i in range(3):
            for j in range(3):
                if(self.grid[i][j] == " "):
                    return False
        print("Oyun berabere") 
        return True 

    def kazananKontrol(self,symbol):
        for i in range(3):
            if(self.grid[i][0] == symbol and
               self.grid[i][1] == symbol and 
               self.grid[i][2] == symbol):
                print(f"{symbol} kazandi!") 
                return True

        for j in range(3):
            if(self.grid[0][j] == symbol and
               self.grid[1][j] == symbol and 
               self.grid[2][j] == symbol):
                print(f"{symbol} kazandi!") 
                return True

        if(self.grid[0][0] == symbol and
           self.grid[1][1] == symbol and
           self.grid[2][2] == symbol):
            print(f"{symbol} kazandi!") 
            return True
        
        if(self.grid[0][2] == symbol and
           self.grid[1][1] == symbol and
           self.grid[2][0] == symbol):
            print(f"{symbol} kazandi!") 
            return True
            

        return False 

class Player:
    def __init__(self,name,symbol):
        self.name = name
        self.symbol = symbol

    def hamleYap(self,board):
        while True:
            print(f"{self.name}'in sirasi ({self.symbol})")

            try:
                row= int(input("Satir giriniz(0-2): "))
                column= int(input("Sütün giriniz(0-2): "))
            except ValueError:
                print("Lütfen sadece sayi giriniz.")
                continue

            if not (0 <= row <= 2 and 0 <= column <= 2):
                print("Gecersiz islem!")  
                continue

            if board.hamleYap1(row, column, self.symbol):
                break
            else:
                print("Bu hücre dolu! Baska hücre seciniz.") 

class Game:
    def __init__(self):
       self.board = Board()  

       name1 = input("1. oyuncunun ismi: ")
       name2 = input("2. oyuncunun ismi: ")  

       self.player1 = Player(name1,"X") 
       self.player2 = Player(name2,"O") 

       self.current_player = self.player1

    def sirayiDegistir(self):
        if (self.current_player == self.player1):
            self.current_player = self.player2
        else:
            self.current_player = self.player1 

    def oyunuBaslat(self):
        print("\n-------X-O-X---------\n")   

        while True:
            self.board.display()   

            self.current_player.hamleYap(self.board)

            if self.board.kazananKontrol(self.current_player.symbol):
                self.board.display()
                print(f"Tebrikler {self.current_player.name},kazandiniz!")
                break

            if self.board.beraberlik():
                self.board.display()
                print("Oyun berabere bitti!")
                break


            self.sirayiDegistir()




# board = Board()
# print(board.hamleYap1(2,2,'X'))
# board.display()
# # print(board.hamleYap1(0,1,'O'))
# # print(board.display())

oyun = Game()
oyun.oyunuBaslat()


