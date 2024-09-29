import random

karakter = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
uzunluk = int (input ("Kaç karekterlik bir şifre istersiniz?"))

sifre = ""

for i in range(uzunluk):
    sifre = sifre + random.choice(karakter)

print(sifre)

