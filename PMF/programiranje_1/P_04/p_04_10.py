print('Program pokazuje listu brojeva')
print('(pocevsi sa 1) i njihove kvadrate.')

pocetak = int(input('Unesite pocetnu vrijednost: '))
kraj = int(input('Unesite zavrsnu vrijednost: '))
    
print()
print('Broj\tKvadrat')
print('---------------')

for broj in range(pocetak, kraj+1):
    kvadrat = broj ** 2
    print(broj, '\t', kvadrat)