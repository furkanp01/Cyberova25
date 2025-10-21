#Basit işlemler yapan hesap makinesi#



a=int(input("""Yapacağınız işlemi seçin:
1-->Toplama
2-->Çıkarma
3-->Çarpma
4-->Bölme
5-->Kalan Bulma
6-->Üs alma
7-->Kök alma
   """))


if a==1:
	c=0
	b=int(input("Kaç sayı gireceksin? "))
	snc=0
	while c!=b:
		d=int(input("Sayıyı girin: "))
		snc=snc+d
		c=c+1
	else:
		print("Sonuç {}".format(snc))
		
if a==2:
	b=int(input("Birinci sayıyı girin: "))
	c=int(input("İkinci sayıyı girin: "))
	snc=b-c
	print("Sonuç: {}".format(snc))


if a==3:
	c=0
	b=int(input("Kaç sayı gireceksin? "))
	snc=1
	while c!=b:
		d=int(input("Sayıyı girin: "))
		snc=snc*d
		c=c+1
	else:
		print("Sonuç: {}".format(snc))

if a==4:
	b=int(input("Bölünen sayıyı girin: "))
	c=int(input("Bölen sayıyı girin: "))
	print("Sonuç: {}".format(b/c))

if a==5:
	b=int(input("Birinci sayıyı girin: "))
	c=int(input("İkinci sayıyı girin: "))
	snc=b%c
	print("{}'nin {}'ye bölümünden kalan: {}".format(b,c,snc))


if a==6:
	b=int(input("Tabanı girin: "))
	c=int(input("Üssü girin: "))
	snc=b**c
	print("{} üssü {} = {}".format(b,c,snc))

if a==7:
	b=int(input("Kökü alınacak sayı? "))
	c=int(input("Kök kaçıncı dereceden? "))
	snc=b**(1/c)
	print("{}'nın {}.dereceden kökü: {}".format(b,c,snc))




	




 	