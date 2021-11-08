import math

V = float(input("Unesite V: "))
O = float(input("Unesite O: "))
L = float(input("Unesite L: "))
t = float(input("Unesite t: "))

O = math.radians(O)

td = 1 / (((2 * V * math.cos(O)) / L) + 1/t)
print (td)