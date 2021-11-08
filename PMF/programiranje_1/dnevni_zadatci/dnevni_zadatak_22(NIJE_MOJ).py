#Za prirodan broj kažemo da je cudan ako je u potpunosti sastavljen od cifara 2 i 3.  
#Korisnik unosi prirodan broj n. Program ispisuje n-ti cudan prirodan broj.

#n = int(input('Unesite prirodan broj n: '))

n = int(input('Unesite prirodan broj n: '))

brojac = 0 

trenutni = 1

while brojac < n:
    trenutni += 1
    cudan = True
    kopija = trenutni
    while kopija > 0:
        if kopija % 10 != 2 and kopija % 10 != 3:
            cudan =  False
        kopija //= 10 
    if cudan:
        brojac += 1

    print(brojac, trenutni, kopija, cudan)

print(trenutni)
