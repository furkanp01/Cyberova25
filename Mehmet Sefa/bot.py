import helper
import random


def Play(table, char):
    c = [-500, -500]   # ilk değer puan, ikinci değer seçilecek index
    for i in range(0, 9):
        if table[i] == "-":
            table[i] = char
            k = MaxMin(table, char, False)
            table[i] = "-"
            if k > c[0]:
                c = [k, i]  

    if c[1] != -500:
        table[c[1]] = char
        helper.printTable(table)
    else:
        table[helper.GetFirstEmptyIndex(table)] = char
        helper.printTable(table)

    
    

                    
            

def MaxMin(table, char, maxmin):
    if maxmin:
        startVal = -500
    else:
        startVal = 500
    controlVal = helper.evaluate(table)
    if controlVal == char:
        return +1
    if controlVal == helper.GetRival(char):
        return -1
    if controlVal == "Berabere":
        return 0
    for i in range(0,9):
        if table[i] == "-":
            if maxmin:
                
                table[i] = char
                newValue = MaxMin(table,char,False)
                startVal = max(startVal,newValue)
                
            else:
                table[i] = helper.GetRival(char)
                newValue = MaxMin(table,char,True)
                startVal = min(startVal,newValue)        
            table[i] = "-"
    return startVal