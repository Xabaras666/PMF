print('Program pokazuje listu brojeva')
print('(pocevsi sa 1) i njihove kvadrate.')

kraj = int(input('Do kojeg broja treba ici? '))
    
print()
print('Broj\tKvadrat')
print('---------------')

for broj in range(1, kraj+1):
    kvadrat = broj ** 2
    print(broj, '\t', kvadrat)