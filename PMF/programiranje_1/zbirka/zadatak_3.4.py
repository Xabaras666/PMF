import math
e = 0.0000000000000001

xC = int(input('x od C: '))
yC = int(input('y od C: '))
r = int(input('pokuprecnik'))
xA = float(input('x od A: '))
yA = float(input('y od A: '))

d = math.sqrt((xA - xC) ** 2 + (yA - yC) ** 2)

if d < r:
    print('Tocka je unutar kruga.')
elif d - r < e and r - d < e:
    print('Tocka je na kruznici')
else:
    print('Tocka je izvan kruga')