import math

n = int(input())
print('Unesite sada ', n, 'Prirodnih brojeva.')

aritmeticka_sredina, geometrijska_sredina, harmonijska_sredina, kvadratna_sredina = 0, 1, 0, 0 

for i in range(n):
    broj = int(input())

    aritmeticka_sredina += broj
    geometrijska_sredina *= broj
    harmonijska_sredina += 1/broj
    kvadratna_sredina += broj ** 2

aritmeticka_sredina /= n
geometrijska_sredina = pow(geometrijska_sredina, 1/n)
harmonijska_sredina = n / harmonijska_sredina
kvadratna_sredina = math.sqrt(kvadratna_sredina / n)

print(aritmeticka_sredina)
print(geometrijska_sredina)
print(harmonijska_sredina)
print(kvadratna_sredina)
