import math
e = 0.0000000001

x1 = float(input('Unesite x prve kruznice: '))
y1 = float(input('Unesite y prve kruznice: '))
x2 = float(input('Unesite x druge kruznice: '))
y2 = float(input('Unesite y druge kruznice: '))
r1 = float(input('Unesite poluprecnik prvog kruga: '))
R2 = r1

d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
dr = r1 * 1.5
if d < dr:
    print ('Kruznice se sjeku')
elif d - dr < e and dr - d < e:
    print('Kruznice se dodiruju')
else:
    print('Kruznice nemaju zajednickih tocki')