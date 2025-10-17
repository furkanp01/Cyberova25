import random #This imports the random module that contains the randint() function
import os
from colorama import Fore, Style, init
init(autoreset=True)

def colorize(cell: str) -> str:
    if cell == "X":
        return Fore.CYAN + Style.BRIGHT + "X" + Style.RESET_ALL
    if cell == "O":
        return Fore.MAGENTA + Style.BRIGHT + "O" + Style.RESET_ALL
    return cell



board= ["-","-","-",
        "-","-","-",
        "-","-","-"]
currentplayer = "X"
winner = None
gamerunning = True

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


#printing the game board

def printboard(board):
    print(f" {colorize(board[0])} │ {colorize(board[1])} │ {colorize(board[2])}")
    print("───┼───┼───")
    print(f" {colorize(board[3])} │ {colorize(board[4])} │ {colorize(board[5])}")
    print("───┼───┼───")
    print(f" {colorize(board[6])} │ {colorize(board[7])} │ {colorize(board[8])}")

#printboard(board)

#take input fot the player 

def playerınput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <=9 and board[inp-1] =="-":
        board[inp-1]= currentplayer
    else:
        print("Player is already in that spot!!(o yer dolu yani!!)")
#check for win or tie

def checkhorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    

def checkrow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    
def checkagle(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
def checktie(board):
    global gamerunning
    if "-" not in board:
        printboard(board)
        print("it is a tie!")
        gamerunning= False 

def checkwin():
    if checkagle(board) or checkhorizontle(board) or checkrow(board):
        printboard(board) 
        print(f"the winner is {winner}") 
        gamerunning = False

# switch the player
def switchplayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    else:

        currentplayer = "X"   
#computer 
def computer(board):
    while currentplayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switchplayer()
            
# check for win or tie again

while gamerunning:
    clear()
    printboard(board)
    print(f"\nSıra: {colorize(currentplayer)}")
    playerınput(board)
    checkwin()
    checktie(board)
    switchplayer()
    computer(board)
    checkwin()
    checktie(board)
