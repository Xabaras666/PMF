x = float(input("Unesite x: "))

if x <= -2:
    rez = -1
elif 0 < x <= 100:
    rez = 1 / (3 + 2/x)
elif x >= 105:
    rez = 200
else:
    rez = 0

print(f"Rezultat je {rez}")


