x = int(input('Unesite vrjednost x: '))

if x <= -2:
    f = 1
elif 0 < x <= 100:
    f = 1 / (3 + 2 / x)
elif x >= 105:
    f = 200
else:
    f = 0

print (f)