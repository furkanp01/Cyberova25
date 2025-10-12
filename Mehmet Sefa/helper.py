def setValue(table,userChar):
    try:
        index = int(input(f"set {userChar}:"))
        if(index < 1 or index > 9):
            raise ValueError
        selected = table[index-1]
        if selected == "-":
            table[index-1]  = userChar
            printTable(table)
        else:
            print("Seçmek istediğin alan dolu yenisini gir")
            return setValue(table,userChar)
            
        
        
    except ValueError:
        print("sadece 1-9 arası sayıları gir")
        return setValue(table,userChar)


def printTable(table):
     for i in range(0, 9, 3):
        print(f"{table[i]} | {table[i+1]} | {table[i+2]}")
        if i < 6:
            print("---------")
            

            
def evaluate(board):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != "-":
            return board[i]
    
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != "-":
            return board[i]
    
    if board[0] == board[4] == board[8] != "-":
        return board[0]
    if board[2] == board[4] == board[6] != "-":
        return board[2]

    if "-" not in board:
        return "Berabere"  

    return None



def GetRival(char):
    l = ""
    if char == "X":
        l = "O"
    if char == "O":
        l = "X" 
    return l



def GetFirstEmptyIndex(table):
    for i in range(0,9):
        if table[i] == "-":
            return i