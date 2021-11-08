# Napisati program koji od korisnika traži unos dva cijela broja x
# i y. Program ispisuje da li je prvi broj veći, manji ili jednak drugom.

x = int(input("Unesite broj x: "))
y = int(input("Unesite broj y: "))

if x > y:
    print("Prvi broj je veći")
elif x < y:
    print("Prvi broj je manji")
elif x == y: # else
    print("Jednaki su")

