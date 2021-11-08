#za bilo koji cijeli broj od 0 do 10 000 koji nije djeljiv sa 2 ili 5,
#moguce je pronaci proizvod sa nekim drugim brojem u kojem je svaka cifra
#1. Program treba pronaci koliko ima cifara u najmanjem takvom proizvodu
#n. Program od korisnika uzima broj n, a ispisuje broj cifara u najmanjem,
#proizvodu n u kojem je svaka cifra 1. U primjeru ispod, kada se broj 3
# pomnozi sa 37 rezultat je 111, i sastoji se od tri jedinice, pa program ispisuje 3.


n = int(input())

#kandidat je broj sacinjen od jedinica
#i provjeravamo da li je on djeljiv sa n
kandidat = 1

#brojac je broj jedinica koji nam treba
brojac = 1

#sve dok broj sacinjen od jedinica nije djeljiva sa n...
while kandidat % n != 0:
#dodaj mu jedinicu na kraj... 
    kandidat = kandidat * 10 + 1
    brojac += 1
    print (kandidat, brojac)

print(brojac)
