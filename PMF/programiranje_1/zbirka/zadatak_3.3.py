x = int(input('Unesite trocifreni broj: '))

if 99 < x < 1000:
    x1 = x // 100
    x2 = (x // 10) % 10
    x3 = x % 10
    print (x1 * x2 * x3)
else:
    print ('Pogresan unos!')