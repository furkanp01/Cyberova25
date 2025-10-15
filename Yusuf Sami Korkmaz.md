oyuntahtasi=[" "for x in range(10)]
def ekranagoster():
  
    print(" "+oyuntahtasi[1] + " " + " " + "|" + " " + oyuntahtasi[2] + " " + "|" + " " + oyuntahtasi[3])
    print("______________")
    print(" "+oyuntahtasi[4] + " " + " " + "|" + " " + oyuntahtasi[5] + " " + "|" + " " + oyuntahtasi[6])
    print("______________")
    print(" "+oyuntahtasi[7] + " " + " " + "|" + " " + oyuntahtasi[8] + " " + "|" + " " + oyuntahtasi[9])

def birharfkoy(harf,konum):    
    oyuntahtasi[konum]=harf
def koyulanalanbosmu(konum):
    return oyuntahtasi[konum]==" "
def tahtadolu():
    if oyuntahtasi.count(" ")>1:
        return False
    else:
        return True
def kazanan(oyuntahtasi,harf):
    return(oyuntahtasi[1]==harf and oyuntahtasi[2]==harf and oyuntahtasi[3]==harf)or(oyuntahtasi[4]==harf and oyuntahtasi[5]==harf and oyuntahtasi[6]==harf )or(oyuntahtasi[7]==harf and oyuntahtasi[8]==harf and oyuntahtasi[9]==harf)or(oyuntahtasi[1]==harf and oyuntahtasi[4]==harf and oyuntahtasi[7]==harf)or(oyuntahtasi[2]==harf and oyuntahtasi[5]==harf and oyuntahtasi[8]==harf)or(oyuntahtasi[3]==harf and oyuntahtasi[6]==harf and oyuntahtasi[9]==harf)or(oyuntahtasi[1]==harf and oyuntahtasi[5]==harf and oyuntahtasi[9]==harf )or(oyuntahtasi[3]==harf and oyuntahtasi[5]==harf and oyuntahtasi[7]==harf)

def oyuncuhareketi():
    konum=int(input("1-9 arasinda bir konum giriniz:"))
    if koyulanalanbosmu(konum):
        birharfkoy("x",konum)
        if kazanan(oyuntahtasi,"x"):
            ekranagoster()
            print("$$$ TEBRİKLER KAZANDINIZ $$$")
            exit()
            ekranagoster()
    else:
        print("Girdiginiz konum dolu lütfen tekrar seçiniz")
        oyuncuhareketi()

def bilgisayarhareketi():
    import random
    müsait_konumlar=[konum for konum,harf in enumerate(oyuntahtasi)if harf !="x" and harf !="0" and konum !=0]
    print(müsait_konumlar)
    hareket=0
    
    for i in müsait_konumlar:
        kopya_Tahta=oyuntahtasi[:]
      
        kopya_Tahta[i]="0"
        if kazanan(kopya_Tahta,"0"): 
            hareket=i
            return hareket
            
    
    köşeler=[]
    for i in müsait_konumlar:
        if i in [1,3,7,9]:
            köşeler.append(i)
    if len(köşeler)>0:
        print(köşeler)
        hareket=random.choice(köşeler)
        print(hareket)
        return hareket
    
    if 5 in müsait_konumlar:
        hareket=5
        return hareket
    
    içerisi=[]

    for i in müsait_konumlar:
        if i in [2,4,6,8]:
            içerisi.append(i)
    if len(içerisi)>0:
        hareket=random.choice(içerisi)
        return hareket 
    
    
def Oyun():
    print("XOX OYUNUNA HOŞGELDİNİZ")
    ekranagoster()

    while not tahtadolu():

        oyuncuhareketi()
        if tahtadolu():
            print("Oyun bitti kazzanan yok!!!")
            exit()

        print("------------------")
        bilgisayarkonum=bilgisayarhareketi()
        birharfkoy("0",bilgisayarkonum)
        if kazanan(oyuntahtasi,"0"):
            ekranagoster()
            print("BİLGİSAYAR KAZANDI TEKRAR DENEYİNİZ!!!")
            exit()

        ekranagoster()
        if tahtadolu():
            print("OYUN BİTTİ KAZANAN YOK !!!")
            exit()

        print("-------------------")

Oyun()
