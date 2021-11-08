n = int(input("Unesite n: "))
m = n

if 99 < n < 1000:
    c = n % 10

    n = n // 10
    b = n % 10

    n = n // 10
    a = n % 10 # radi i a = n

    print(f"Proizvod cifara broja {m} je {a * b * c}")

