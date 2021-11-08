import random

n = int(input('Gornja granica: '))
slucajan_broj = random.randrange(1, n + 1)

predikcija = int(input('Predikcija: '))

while predikcija != slucajan_broj:
    predikcija = int(input('Niste pogodili, pokusajte ponovo: '))


print('Pogodili ste')