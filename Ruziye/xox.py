oyunTahtası=list(" " for x in range(10)) 
def screen():
    print(f"{oyunTahtası[1]}|{oyunTahtası[2]}|{oyunTahtası[3]}")
    print(f"_________")
    print(f"{oyunTahtası[4]}|{oyunTahtası[5]}|{oyunTahtası[6]}")
    print(f"_________")
    print(f"{oyunTahtası[7]}|{oyunTahtası[8]}|{oyunTahtası[9]}")
    return
print(f"""Oyun tahtası şu şekilde:
1\t2\t3\n4\t5\t6\n7\t8\t9""")
def hamle(harf,konum):
    oyunTahtası[konum]=harf

def kazanmaKontrol(harf):
    win=[[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]
    for a,b,c in win:
        if oyunTahtası[a]==oyunTahtası[b]==oyunTahtası[c]==harf:
            return True
    return False
def konumKontrol(konum):
    return oyunTahtası[konum]==" "

def hamleAl(aktifOyuncu):
    while True:
        try:
            pozisyon_girdisi=input(f"Sıra{aktifOyuncu} oyuncusunda.Bir poziyon(1-9) girin: ")
            konum=int(pozisyon_girdisi)
            if 1<= konum<=9:
                if konumKontrol(konum):
                    return konum
                else:
                    print("Burası dolu.Başka bir uyer seçin.")
            else:
                print("Lütfen 1 ile 9 arası bir sayı girin.")
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı girin.")
def tahtaDolumu():
    for i in range(1, 10):
        
        if oyunTahtası[i] == " ": 
            return False
    return True
aktifOyuncu = "X"
oyunDevamEdiyor = True
while oyunDevamEdiyor:
    screen()
    secilen_konum=hamleAl(aktifOyuncu)
    hamle(aktifOyuncu, secilen_konum)
    if kazanmaKontrol(aktifOyuncu):
        screen()
        print(f"Tebrikler! {aktifOyuncu} oyuncusu kazandı!")
        oyunDevamEdiyor=False
        continue
    if tahtaDolumu():
        screen()
        print("Tahta doldu! Oyun berabere!")
        oyunDevamEdiyor=False
        continue
    if aktifOyuncu=="X":
        aktifOyuncu="O"
    else:
        aktifOyuncu="X"

print("\nOyun Bitti.")
