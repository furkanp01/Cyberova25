import tkinter as tk
from tkinter import messagebox

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("XOX Oyunu")
        self.root.resizable(False, False)
        
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        
        self.create_widgets()

    def create_widgets(self):
        # 3x3 oyun alanı için butonları oluştur
        button_frame = tk.Frame(self.root)
        button_frame.pack()
        
        for i in range(9):
            button = tk.Button(
                button_frame, 
                text="", 
                font=('Helvetica', 24, 'bold'),
                width=5, 
                height=2,
                command=lambda i=i: self.on_button_click(i)
            )
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)
            
        # Reset butonu
        reset_button = tk.Button(
            self.root, 
            text="Yeniden Başlat", 
            font=('Helvetica', 12),
            command=self.reset_game
        )
        reset_button.pack(pady=10)

    def on_button_click(self, index):
        # Buton boşsa ve oyun bitmemişse işlem yap
        if self.buttons[index]["text"] == "" and self.check_winner() is None:
            self.buttons[index]["text"] = self.current_player
            self.buttons[index].config(disabledforeground=self.get_player_color())
            self.board[index] = self.current_player
            
            winner = self.check_winner()
            if winner:
                if winner == "Berabere":
                    messagebox.showinfo("Oyun Bitti", "Oyun berabere!")
                else:
                    messagebox.showinfo("Oyun Bitti", f"Tebrikler! Oyuncu '{winner}' kazandı!")
                self.disable_all_buttons()
            else:
                self.switch_player()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def get_player_color(self):
        return "red" if self.current_player == "O" else "blue"

    def check_winner(self):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Yatay
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Dikey
            (0, 4, 8), (2, 4, 6)             # Çapraz
        ]
        
        for condition in win_conditions:
            if (self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] and 
                self.board[condition[0]] != ""):
                return self.board[condition[0]]
        
        if "" not in self.board:
            return "Berabere"
            
        return None

    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="", state=tk.NORMAL)

    def disable_all_buttons(self):
        for button in self.buttons:
            button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()