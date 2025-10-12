import helper

def main():
    playerChar = input("X veya O: ")

    board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

    if playerChar != "X" and playerChar != "O":
        print("Lütfen sadece X veya O girin!")
    else:
        helper.printTable(board)
        
    while True:
     helper.setValue(board,playerChar)



if __name__ == "__main__":
    main()