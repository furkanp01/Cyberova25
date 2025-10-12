import helper
import bot
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
       helper.evaluate(board)
       if current == playerChar:
           helper.setValue(board,playerChar)
           current = "O"
       if current != playerChar:
           bot.Play(board,current) 
           print("sıra botta")
           current = "X"
         



if __name__ == "__main__":
    main()