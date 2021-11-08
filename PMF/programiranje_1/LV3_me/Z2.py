#funkcija f se definise po segmentima sa {{{x**2             x<=0
#                                         {{(100-x)/x**4     0<x<= 100
#                                          {200              100<x

x = int(input("Unesite cijeli broj: "))

if x <= 0:
    print (x ** 2)
elif 0 < x <= 100:
    print ((100-x)/(x**4))

elif x > 100:
    print(200)