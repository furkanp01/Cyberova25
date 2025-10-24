import tkinter as tk
import tkinter.messagebox

counter = 0

root = tk.Tk()
root.title("XOX")
root.geometry("400x400")




def restart():
    global counter
    counter = 0
    for i in range (3):
        for j in range (3):
            buttons[i][j]["text"] = ""

def check_winner():

    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return buttons[i][0]["text"]  # X veya O kazandı

    for j in range(3):
        if buttons[0][j]["text"] == buttons[1][j]["text"] == buttons[2][j]["text"] != "":
            return buttons[0][j]["text"]  # X veya O kazandı

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return buttons[0][0]["text"]  # X veya O kazandı
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return buttons[0][2]["text"]  # X veya O kazandı

    full = all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3))
    if full:
        return "draw"





    return None

def click(i, j):
    global counter

    if buttons[i][j]["text"] == "":
        # X veya O yaz
        if counter % 2 == 0:
            buttons[i][j]["text"] = "X"
        else:
            buttons[i][j]["text"] = "O"
        counter += 1


        winner = check_winner()
        if winner:
            tkinter.messagebox.showinfo("Winner", winner)
            restart()


buttons = \
[[None ,None,None],
[None,None,None],
[None,None,None],
]


#main

for i in range(3):
    for j in range(3):
        btn= tk.Button(root,text="",command= lambda i=i, j=j: click(i,j))
        btn.grid(row=i,column=j,sticky="nsew")
        buttons[i][j] = btn
for i in range(3):
    root.grid_rowconfigure(i,weight=1)
    root.grid_columnconfigure(i,weight=1)


root.mainloop()