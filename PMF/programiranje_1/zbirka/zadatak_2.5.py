import math

b = int(input('Unesite stranicu b: '))
c = int(input('Unesite stranicu c: '))
alfa = int(input('Unesite alfa: '))

alfa = alfa * (math.pi / 180)

print (math.sqrt((b ** 2) + (c ** 2) - (2 * b * c * math.cos(alfa))))