import helper
import bot
import os
def main():
    playerChar = input("X veya O: ")

    board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

    if playerChar != "X" and playerChar != "O":
        print("Lütfen sadece X veya O girin!")
        return main()
    else:
        helper.printTable(board)

    current = "X"
    while True:
       
       
       if  helper.evaluate(board) == None:    
        if current == playerChar:

            helper.setValue(board,playerChar)
            current = helper.GetRival(playerChar)
        else:
            bot.Play(board,current) 
            current = helper.GetRival(current)
        os.system("cls")
        helper.printTable(board)
       else:
           print("Oyun bitti kazanan: ",helper.evaluate(board) )
           break

        
    

         



if __name__ == "__main__":
    main()