import math

x = float(input('Unesite x: '))
y = float(input('Unesite y: '))
alfa = float(input('Unesite alfa: '))

alfa = math.radians(alfa)

V0 = math.sqrt(((x ** 2) * 9.80665) / (x * math.sin(2 * alfa)- 2 * y * (math.cos(alfa) ** 2)))

print (V0)