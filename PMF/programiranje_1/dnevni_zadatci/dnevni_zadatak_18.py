#Korisnik unosi prirodan broj n.  U jednom potezu, od broja se oduzima 
# njegova najveća cifra. U narednom potezu, od rezultata se oduzima 
# njegova najveća cifra itd. Program treba odrediti i ispisati koliko 
# poteza je potrebno da bi se došlo do nule. Na primjer, za broj 24 
# potrebno je pet poteza (24→20→18→10→9→0).

x = int(input('Unesite jedan prirodan broj x: '))
z = x
l = [0]
a = 0
b = 0

while x > 0:
    l.clear()
    x -= a
    y = x % 10
    l.append(y)
    z //= 10
    y = z % 10
    l.append(y)
    a = max(l)
    z = x
    b += 1
print(f"Broj potrebnih poteza je: {b - 1}")