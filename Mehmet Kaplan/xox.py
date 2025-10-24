class XOXGame:
    def __init__(self):
        """Oyunu başlat ve tahtayı hazırla"""
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        
    def display_board(self):
        """Oyun tahtasını konsola yazdır"""
        print("\n" + "="*13)
        print("| " + self.board[0] + " | " + self.board[1] + " | " + self.board[2] + " |")
        print("| " + self.board[3] + " | " + self.board[4] + " | " + self.board[5] + " |")
        print("| " + self.board[6] + " | " + self.board[7] + " | " + self.board[8] + " |")
        print("="*13)
        print("Hamle yapmak için 1-9 arası sayı girin")
        print("1|2|3")
        print("4|5|6")
        print("7|8|9")
        
    def make_move(self, position):
        """Belirtilen pozisyona hamle yap"""
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        return False
        
    def check_winner(self):
        """Kazanan oyuncuyu kontrol et"""
        # Kazanma kombinasyonları
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Yatay
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Dikey
            [0, 4, 8], [2, 4, 6]              # Çapraz
        ]
        
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == 
                self.board[combo[2]] != ' '):
                return self.board[combo[0]]
        return None
        
    def is_board_full(self):
        """Tahta dolu mu kontrol et"""
        return ' ' not in self.board
        
    def switch_player(self):
        """Oyuncu değiştir"""
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        
    def get_player_input(self):
        """Oyuncudan geçerli hamle al"""
        while True:
            try:
                move = input(f"\n{self.current_player} oyuncusu, hamlenizi yapın (1-9): ")
                position = int(move) - 1
                
                if 0 <= position <= 8:
                    if self.make_move(position):
                        return True
                    else:
                        print("Bu pozisyon zaten dolu! Başka bir pozisyon seçin.")
                else:
                    print("Lütfen 1-9 arası bir sayı girin!")
                    
            except ValueError:
                print("Geçersiz giriş! Lütfen bir sayı girin.")
                
    def play_game(self):
        """Ana oyun döngüsü"""
        print("🎮 XOX Oyununa Hoş Geldiniz!")
        print("İki oyuncu arasında oynanan klasik oyun.")
        
        while True:
            self.display_board()
            
            # Hamle al
            self.get_player_input()
            
            # Kazanan kontrolü
            winner = self.check_winner()
            if winner:
                self.display_board()
                print(f"\n🎉 Tebrikler! {winner} oyuncusu kazandı!")
                break
                
            # Beraberlik kontrolü
            if self.is_board_full():
                self.display_board()
                print("\n🤝 Oyun berabere! Tahta dolu.")
                break
                
            # Oyuncu değiştir
            self.switch_player()
            
    def reset_game(self):
        """Oyunu sıfırla"""
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

def main():
    """Ana fonksiyon"""
    while True:
        game = XOXGame()
        game.play_game()
        
        # Tekrar oynama seçeneği
        play_again = input("\nTekrar oynamak ister misiniz? (e/h): ").lower()
        if play_again not in ['e', 'evet', 'y', 'yes']:
            print("Oyun bitti. İyi günler! 👋")
            break

if __name__ == "__main__":
    main()
