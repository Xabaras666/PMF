# Napisati program koji od korisnika traži unos dva realna broja x
# i y. Program ispisuje da li je prvi broj veći, manji ili jednak drugom.

x = float(input("Unesite broj x: "))
y = float(input("Unesite broj y: "))

epsilon = 0.00000001

if x - y < epsilon and y - x < epsilon:
    print("Jednaki su")
elif x > y:
    print("Prvi broj je veći")
elif x < y:
    print("Prvi broj je manji")

# x - y < epsilon and y - x < y epsilon
# --------(1)--------------------------
