import math

a = float(input('Unesite a: '))
b = float(input('Unesite b: '))
c = float(input('Unesite c: '))
theta = float(input('Unesite theta: '))
phi = float (input('Unesite phi: '))

theta = theta * (math.pi / 180)
phi = phi *(math.pi / 180)

x = a * math.sin(theta) * math.cos(phi)
y = b * math.cos(theta) * math.sin(phi)
z = c * math.sin(theta)

print (x)
print (y)
print (z  )