#program trazi od korisnika da unese n broj
# program ispisuje n-ti prosti broj

n = int(input('Unesite n: '))

trenutni_broj = 2
brojac_prostih = 0


while brojac_prostih < n:
    x = trenutni_broj
    prost = True
    broj_djelilaca = 0
    for i in range(2, x):
        if x % i == 0:
            prost = False
            break

    if prost  == True:
        brojac_prostih += 1

    trenutni_broj += 1

print (trenutni_broj-1)
