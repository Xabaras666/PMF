print('Unesite brojeve (-1 oznacava kraj unosa): ')
unos, suma = 0, 0

while True:
    unos = int(input())

    if unos == -1:
        break

    zadnja_cifra = unos % 10
    suma += zadnja_cifra

print('Suma zadnjih cifara unesenih brojeva je: ', suma)