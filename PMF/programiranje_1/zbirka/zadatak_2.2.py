import math

alfa = int(input('Unesite alfa: '))
beta = int(input('Unesite beta: '))
c = float(input('Unesite c: '))

gama = 180 - alfa - beta

alfa = alfa * (math.pi / 180)
beta = beta * (math.pi / 180)
gama = gama * (math.pi / 180)

r = c * ((math.sin(alfa / 2) * math.sin(beta / 2)) / (math.cos(gama / 2))) 

print(r)