x = int(input('Unesite petocifren  broj:'))

if 9999 < x < 100000:
    x5 = x % 10
    x4 = (x // 10) % 10
    x3 = (x // 100) % 10
    x2 = (x // 1000) % 10
    x1 = x // 10000 
    max = x1
    if x2 > max:
        max = x2
    if x3 > max:
        max = x3
    if x4 > max:
        max = x4
    if x5 > max:
        max = x5

    min = x5
    if x4 < min:
        min = x4
    if x3 < min:
        min = x3
    if x2 < min:
        min = x2
    if x1 < min:
        min = x1
    print (max - min)
else:
    print ('Pogresan unos.')