import tkinter  #Bu kütüphaneyi oyun penceresi oluşturabilmek için kullandım.
from tkinter import messagebox #Bu kütüphaneyi pencere açıp berabere veya kazandınız gibi mesajları iletebilmek için kullandım.
import random   #Bu kütüphaneyi bilgisayarın rastgele sayılar üretebilmesi için kullandım.

class XOX:  #Oyunumun bütün özelliklerini bir sınıf içinde topladım.
    def __init__(self, root, size=6): #Oyun tablomuz 6 satır ve 6 sütundan oluşacak şekilde ayarladım.
        self.root = root
        self.size = size
        self.WIN_LENGTH = 3  # Kazanmak için yanyana veya çapraz şekilde 3 tane aynı sembol olmalı o yüzden bunu en başta belirledim.
        
        self.root.title(f"{self.size}x{self.size} XOX Oyunu") # Penceremin başlığını oyunun boyutuna göre değişebilir yaptım.
        self.root.resizable(False, False) # Pencerenin boyutunun değiştirilmesini engelledim.
        
        # Oyuncunun oyuna X lemi yoksa O ilemi başlayacağını bilmiyorum hangisini tercih ederse diğeri bilgisayara kalıyor o yüzden başlangıçta ikisinede boş değerini atadım.
        self.player_symbol = None
        self.computer_symbol = None # Bilgisayarın sembolünü de başlangıçta boş olarak ayarladım.
        self.difficulty = None   # Oyunun zorluk seviyesini oyuncu seçeceği için başlangıçta boş olmalı.
        self.current_player = "X" # kural gereği oyuna herzaman X le başlandığı için ilk başlayan kullanıcıyı X olarak seçtim.
        self.board = [""] * (self.size * self.size) # 36 tane boş kareden oluşan oyun tahtamı bir liste olarak tasarladım.
        self.buttons = [] # Ekranda oluşturacağım butonları bu listede tutacağım.
        self.game_over = False # Oyunun bitip bitmediğini kontrol etmek için bir değişken, başlangıçta False.

        # Bütün görsel elemanları (butonlar, yazılar vs.) bu ana çerçevenin içine koyacağım. Bu, ekranı temizlemeyi kolaylaştırıyor.
        self.main_frame = tkinter.Frame(root)
        self.main_frame.pack()

        #Başlangıç ekranını oluşturacak fonksiyonu çağırdım.
        self.create_setup_screen()

    # Bu fonksiyon, oyunun en başında oyuncuya sembol ve zorluk seçimi yaptırdığım ekranı oluşturuyor.
    def create_setup_screen(self):
        # Eğer "Yeni Oyun" butonuna basılırsa, eski ekrandaki her şeyi silmek için bu döngüyü kullandım.
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Oyuncuya ne yapması gerektiğini söyleyen bilgilendirme yazıları ekledim.
        tkinter.Label(self.main_frame, text="Hangi sembolle oynamak istersin?", font=('Helvetica', 14)).pack(pady=10)
        
        # Butonların yanyana durması için onlara özel bir çerçeve oluşturdum.
        symbol_frame = tkinter.Frame(self.main_frame)
        symbol_frame.pack(pady=5)
        
        # X ve O butonlarını oluşturdum. 
        tkinter.Button(symbol_frame, text="X (İlk Başlar)", font=('Helvetica', 12), command=lambda: self.set_player_symbol("X")).pack(side="left", padx=10)
        tkinter.Button(symbol_frame, text="O (İkinci Başlar)", font=('Helvetica', 12), command=lambda: self.set_player_symbol("O")).pack(side="left", padx=10)

        tkinter.Label(self.main_frame, text="Zorluk Seviyesini Seç", font=('Helvetica', 14)).pack(pady=10)
        
        # Oyuncunun seçtiği zorluğu saklamak için bir tkinter değişkeni oluşturdum.
        self.difficulty_var = tkinter.StringVar(value="Kolay") #Eğer zorluk seviyesi seçilmezsse kolay seçilmiş kabul edilecek.
        radio_frame = tkinter.Frame(self.main_frame)
        radio_frame.pack(pady=5)
        
        # Radyo butonları ile oyuncunun sadece bir zorluk seçebilmesini sağladım.
        tkinter.Radiobutton(radio_frame, text="Kolay", variable=self.difficulty_var, value="Kolay", font=('Helvetica', 10)).pack(side="left")
        tkinter.Radiobutton(radio_frame, text="Orta", variable=self.difficulty_var, value="Orta", font=('Helvetica', 10)).pack(side="left")
        tkinter.Radiobutton(radio_frame, text="Zor", variable=self.difficulty_var, value="Zor", font=('Helvetica', 10)).pack(side="left")

    # Oyuncu sembol seçimi butonlarından birine tıkladığında bu fonksiyon çalışır.
    def set_player_symbol(self, symbol):
        self.player_symbol = symbol # Oyuncunun seçtiği sembolü kaydettim.
        self.computer_symbol = "O" if symbol == "X" else "X" # Oyuncu X'i seçtiyse bilgisayara O'yu, değilse X'i verdim.
        self.difficulty = self.difficulty_var.get() # Radyo butonlarından seçilen zorluğu aldım.
        self.start_game() # Oyunu başlattım.

    # Bu fonksiyon, kurulum ekranını temizleyip oyun tahtasını ekrana getirir.
    def start_game(self):
        # Kurulum ekranındaki butonları ve yazıları temizledim.
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Oyun tahtasını oluşturacak fonksiyonu çağırdım.
        self.create_board_widgets()
        
        # Bu kontrol önemli: Eğer oyuncu 'O' (ikinci) olmayı seçtiyse, ilk hamleyi bilgisayar ('X') yapmalı.
        if self.current_player == self.computer_symbol:
            self.computer_move()

    # Bu fonksiyon, 36 tane tıklanabilir butondan oluşan oyun alanını oluşturur.
    def create_board_widgets(self):
        button_frame = tkinter.Frame(self.main_frame)
        button_frame.pack()
        
        # Bu döngüyle 36 butonu tek tek oluşturup 6x6'lık bir ızgara şeklinde yerleştirdim.
        for i in range(self.size * self.size):
            button = tkinter.Button(button_frame, text="", font=('Helvetica', 14, 'bold'), width=4, height=2, command=lambda i=i: self.on_button_click(i))
            button.grid(row=i // self.size, column=i % self.size)
            self.buttons.append(button) # Oluşturduğum her butonu listeme ekledim ki sonra onlara erişebileyim.
            
        # Oyunu en baştan başlatmak için bir "Yeni Oyun" butonu ekledim.
        reset_button = tkinter.Button(self.main_frame, text="Yeni Oyun", font=('Helvetica', 12), command=self.reset_game)
        reset_button.pack(pady=10)

    # Oyuncu tahtadaki bir butona tıkladığında bu fonksiyon çalışır.
    def on_button_click(self, index):
        # Bu kontrol çok önemli: Sadece oyun bitmediyse, sıra oyuncudaysa ve tıklanan kutu boşsa hamle yapmasına izin veriyorum.
        if not self.game_over and self.current_player == self.player_symbol and self.board[index] == "":
            self.update_board(index, self.player_symbol) 
            
            # Her hamleden sonra kontrol ediyorum:
            if self.check_winner(self.player_symbol): # Oyuncu kazandı mı?
                self.end_game(f"Tebrikler, kazandın!")
            elif "" not in self.board: # Tahta doldu mu (berabere mi)?
                self.end_game("Oyun berabere bitti!")
            else: # Oyun devam ediyorsa
                self.switch_player() # Sırayı bilgisayara verdim.
                # Şimdi bilgisayara oynamasını söylüyorum ve 500ms beklemesini sağlıyorum.
                self.root.after(500, self.computer_move)

    # Bu fonksiyon, bilgisayarın hamle yapma sürecini yönetir.
    def computer_move(self):
        # Oyun zaten bittiyse bilgisayarın hamle yapmasını engelliyorum.
        if self.game_over:
            return

        # Seçilen zorluğa göre bilgisayarın hangi "beyni" kullanacağını belirledim.
        if self.difficulty == "Kolay":
            move_index = self.get_easy_move()
        elif self.difficulty == "Orta":
            move_index = self.get_medium_move()
        elif self.difficulty == "Zor":
            move_index = self.get_hard_move()
        
        # Eğer bilgisayar oynayacak bir yer bulabildiyse...
        if move_index is not None:
            self.update_board(move_index, self.computer_symbol) # Bilgisayarın hamlesini tahtaya işledim.
            
            # Bilgisayarın hamlesinden sonra da kazanma veya berabere kalma durumunu kontrol ettim.
            if self.check_winner(self.computer_symbol):
                self.end_game(f"Bilgisayar kazandı!")
            elif "" not in self.board:
                self.end_game("Oyun berabere bitti!")
            else: # Oyun hala devam ediyorsa...
                self.switch_player() # Sırayı tekrar oyuncuya verdim.
    
    # Kolay seviye bilgisayar: Hiç düşünmeden, boş bulduğu yerlerden rastgele birini seçer.
    def get_easy_move(self):
        empty_cells = [i for i, val in enumerate(self.board) if val == ""]
        return random.choice(empty_cells) if empty_cells else None

    # Orta seviye bilgisayar: Akıllı oynamaya başlar.
    def get_medium_move(self):
        # 1. Öncelik: "Ben bir sonraki hamlede kazanabilir miyim?" diye kontrol eder. Varsa o hamleyi yapar.
        for i in range(self.size * self.size):
            if self.board[i] == "":
                self.board[i] = self.computer_symbol
                if self.check_winner(self.computer_symbol):
                    self.board[i] = ""
                    return i
                self.board[i] = ""
        
        # 2. Öncelik: "Rakibim bir sonraki hamlede kazanabilir mi?" diye kontrol eder. Varsa o hamleyi engelleyerek savunma yapar.
        for i in range(self.size * self.size):
            if self.board[i] == "":
                self.board[i] = self.player_symbol
                if self.check_winner(self.player_symbol):
                    self.board[i] = ""
                    return i
                self.board[i] = ""

        # 3. Eğer kazanma veya engelleme durumu yoksa, kolay seviyedeki gibi rastgele bir hamle yapar.
        return self.get_easy_move()

    # Zor seviye bilgisayar: Orta seviyenin tüm yeteneklerine sahip, ek olarak basit bir stratejisi var.
    def get_hard_move(self):
        # Önce orta seviyedeki gibi kazanma veya engelleme hamlesi arar.
        move = self.get_medium_move()
        # Eğer bu fonksiyon rastgele bir hamle değil de, gerçekten bir kazanma/engelleme hamlesi bulduysa, onu oynar.
        if move is not None and self.board[move] == "":
            temp_board_computer = self.board[:]
            temp_board_computer[move] = self.computer_symbol
            temp_board_player = self.board[:]
            temp_board_player[move] = self.player_symbol
            if self.check_winner(self.computer_symbol, board=temp_board_computer) or self.check_winner(self.player_symbol, board=temp_board_player):
                return move

        # Eğer kazanma/engelleme hamlesi yoksa, rastgele oynamak yerine stratejik bir hamle yapar.
        # Stratejim: Tahtanın merkezine en yakın boş kareyi oynamak.
        empty_cells = [i for i, val in enumerate(self.board) if val == ""]
        center = (self.size * self.size) / 2
        empty_cells.sort(key=lambda i: abs(i - center))
        return empty_cells[0] if empty_cells else None

    def update_board(self, index, player):
        self.board[index] = player
        self.buttons[index].config(text=player, state=tkinter.DISABLED, disabledforeground="blue" if player == "X" else "red")
    
    # Sırayı diğer oyuncuya geçiren basit bir fonksiyon.
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
    
    # Oyunun kazanma mantığının olduğu yer. Yatay, dikey ve çapraz olarak 3'lü var mı diye tüm tahtayı tarar.
    def check_winner(self, player, board=None):
        # Bu fonksiyonu, hem mevcut tahtayı hem de bilgisayarın denediği hayali tahtaları kontrol edebilmesi için esnek yaptım.
        if board is None:
            board = self.board
        
        # Yatay kontrol
        for r in range(self.size):
            for c in range(self.size - (self.WIN_LENGTH - 1)):
                if all(board[r * self.size + c + i] == player for i in range(self.WIN_LENGTH)):
                    return True
        # Dikey kontrol
        for c in range(self.size):
            for r in range(self.size - (self.WIN_LENGTH - 1)):
                if all(board[(r + i) * self.size + c] == player for i in range(self.WIN_LENGTH)):
                    return True
        # Çapraz kontrol (Soldan sağa)
        for r in range(self.size - (self.WIN_LENGTH - 1)):
            for c in range(self.size - (self.WIN_LENGTH - 1)):
                if all(board[(r + i) * self.size + (c + i)] == player for i in range(self.WIN_LENGTH)):
                    return True
        # Çapraz kontrol (Sağdan sola)
        for r in range(self.size - (self.WIN_LENGTH - 1)):
            for c in range(self.WIN_LENGTH - 1, self.size):
                if all(board[(r + i) * self.size + (c - i)] == player for i in range(self.WIN_LENGTH)):
                    return True
        return False

    # Oyun bittiğinde bu fonksiyon çalışır.
    def end_game(self, message):
        self.game_over = True # Oyunun bittiğini belirttim.
        messagebox.showinfo("Oyun Bitti", message) # Ekrana sonuç mesajını çıkardım.
        # Oyun bittiği için artık hiçbir butona tıklanmaması için hepsini devre dışı bıraktım.
        for button in self.buttons:
            button.config(state=tkinter.DISABLED)

    # "Yeni Oyun" butonuna basıldığında her şeyi en başa döndüren fonksiyon.
    def reset_game(self):
        # Bütün oyun değişkenlerini ilk hallerine, yani 'None' veya başlangıç değerlerine döndürdüm.
        self.player_symbol = None
        self.computer_symbol = None
        self.difficulty = None
        self.current_player = "X"
        self.board = [""] * (self.size * self.size)
        self.buttons = []
        self.game_over = False
        # Her şeyi sıfırladıktan sonra, kullanıcıya tekrar sembol ve zorluk seçtirmek için başlangıç ekranını yeniden oluşturdum.
        self.create_setup_screen()


# Bu standart Python bloğu, programımın doğrudan çalıştırıldığında başlamasını sağlar.
if __name__ == "__main__":
    root = tkinter.Tk() # Ana penceremi oluşturdum.
    app = XOX(root, size=6) # Yukarıda tasarladığım XOX sınıfından bir oyun nesnesi yarattım.
    root.mainloop() # Pencerenin ben kapatana kadar ekranda kalmasını ve olayları (tıklama vb.) dinlemesini sağladım.