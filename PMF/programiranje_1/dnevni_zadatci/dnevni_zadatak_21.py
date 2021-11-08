#Napisati program koji simulira bacanje novcica.  
# Korisnik bira jedan od brojeva 0 (glava) ili 1 (pismo). 
# Program slucajno generiše jedan od ishoda,te ukoliko je korisnik 
# ispravno pogodio, program traži novi unos. 
# Nakon što korisnik ne pogodi ishod bacanja, 
# program prekida sa radom i ispisuje broj pogodjenih bacanja.
import random

n = int(input('Broj 0 = glava, broj 1 = pismo:'))
tocna_bacanja = 0
while True:
    broj = random.randint(0, 1)
    print(broj)
    if broj == n:
        n = int(input('Broj 0 = glava, broj 1 = pismo:'))
        tocna_bacanja += 1
    else:
        break

print(f"Broj pogodnjenih bacanja je: {tocna_bacanja}")

