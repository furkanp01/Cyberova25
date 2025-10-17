class board:
    def __init__(self):
        self.cells = [" "," "," "," "," "," "," "," "," "] 
        
    def choice(self,choice,player):
        mark = "X" if player == 1 else "O"
        self.cells[choice - 1] = mark
            
    def display(self):
        for j in range(0, 9, 3):
            print(f" {self.cells[j]} | {self.cells[j + 1]} | {self.cells[j + 2]}")

            if j < 6: 
                print("---+---+---")
                
    def situation(self):
        wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]
        ]
        for a,b,c in wins:
            if self.cells[a] == self.cells[b] == self.cells[c] != " ":
                return True
        return False
        
    def is_draw(self):
        return " " not in self.cells

class start:
    def __init__(self):
        print("welcome to tic tac toe game")
        self.game1 = board()


        self.game1.display() 

        while True:
            game_over = False
            
            while True:
                print("\nplayer X, choose a cell between(1-9):")
                player = 1
                choose = int(input()) 
                
                if not (1 <= choose <= 9):
                    print("Hata: Seçim 1 ile 9 arasında olmalıdır.")
                    continue
                
                if(self.game1.cells[choose - 1] != " "):
                    print("this cell is already taken")
                    continue
                else:
                    self.game1.choice(choose,player)
                    self.game1.display()
                    
                    if(self.game1.situation() == True):
                        print("player X is won the game")
                        game_over = True
                        break
                    
                  
                    if(self.game1.is_draw() == True): 
                        print("Game Draw! (Berabere)")
                        game_over = True
                        break

                    break 
            
            if(game_over == True):
                break 

            while True:
                print("\nplayer O, choose a cell between(1-9)")
                player = 2
                choose = int(input()) 

                if not (1 <= choose <= 9):
                    print("it should be between (1-9)")
                    continue
                    
                if(self.game1.cells[choose - 1] != " "):
                    print("this cell is already taken")
                    continue
                else:
                    self.game1.choice(choose,player)
                    self.game1.display()
                    
                    if(self.game1.situation() == True):
                        print("player O is won the game")
                        game_over = True
                        break
                    
                  
                    if(self.game1.is_draw() == True): 
                        print("Game Draw!")
                        game_over = True
                        break

                    break 

            if(game_over == True):
                break 
                
game = start()