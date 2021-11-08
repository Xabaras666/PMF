#Korisnik unosi prirodan broj n. Program ispisuje:
#1. Supalj kvadrat stranice n sastavljen od zvijezdica.
#2. Suplju naopaku piramidu visine n sa okvirom od zvijezdica.
#3. baklavu visine 2*n 

n = int(input("Unesite prirodan broj n:"))


for i in range(0, n ):
    for j in range (0, n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=' ')
        else:
            print(" ", end=' ')

    print()

print()


for i in range(0, n):
    for j in range (0, 2*n-1):
        if i == 0 or i == j or i + j == 2*n-2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

print()


for i in range(0, 2 * n):
    for j in range(0, 2 * n - 1):
        #if i + 1 == n or i + j == n + 2 or j - i == n-1 or i - j == n: 
        if  j - i == n - 1 or j + i == n - 1 or i - j == n or i + j == n * 2 + n -2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    

