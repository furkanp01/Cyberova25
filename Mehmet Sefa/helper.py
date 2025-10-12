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
            return setValue(table,userChar)
            
        
        
    except ValueError:
        return setValue(table,userChar)


def printTable(table):
     for i in range(0, 9, 3):
        print(f"{table[i]} | {table[i+1]} | {table[i+2]}")
        if i < 6:
            print("---------")