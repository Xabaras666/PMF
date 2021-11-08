a = int(input("Unesite trocifren broj> "))
if a > 99 and a < 1000:
    a3 = a % 10
    a2 = (a // 10) % 10
    a1 = (a // 100)
    proizvod = a1 * a2 * a3
    print (proizvod)
else:
    print("Broj nije trocifren")