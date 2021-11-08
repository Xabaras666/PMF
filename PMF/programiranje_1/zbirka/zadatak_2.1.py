import math

alfa = int(input("Unesite alfa: "))
n = float(input('Unesite n: '))
k = float(input('Unesite k: '))
h = float(input('Unesite h: '))

r = alfa * (math.pi / 180)

a = ((2 * k ** (2 / 3)) / (math.sin(r) * math.sqrt(h + n))) * math.cos(r)

print (a)