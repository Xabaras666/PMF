import math

x = int(input('Unesite x: '))
y = int(input('Unesite y: '))

r = math.sqrt(x ** 2 + y ** 2)

phi = math.degrees(math.atan2(y, x))

print (r)
print(phi)
