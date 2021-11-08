import math 

V0 = float(input('Unesite pocetno ubrzanje: '))
R = float (input('Unesite raspon: '))
alfa = int(input('Unesite ugao alfa: '))

alfa = math.radians(alfa)

g = ((V0 ** 2) / R ) * math.sin(2 * alfa)

print (g)