# Napisati program koji od korisnika traži da unese četverocifren
# broj. Program provjerava da li je uneseni broj četverocifren, te ispisuje
# njegovu najveću cifru.

x = int(input("Unesite četverocifren broj:"))

if 999 < x < 10000:
    # sada je broj 1234, ostatak sa 10 je 4
    d = x % 10

    # odbijemo zadnju cifru, dobijemo 123
    x = x // 10
    # ostatak sa 10 je 3
    c = x % 10

    # odbijemo zadnju cifru, dobijemo 12
    x = x // 10
    # ostatak sa 10 je 2
    b = x % 10

    # odbijemo zadnju cifru, dobijemo 1
    x = x // 10
    # ostatak pri dijeljenju sa 10 je 1
    a = x % 10

    # TODO Implementirati bez funkcije max
    najveca = max(a, b, c, d)
    print(najveca)
else:
    print("Broj nije četverocifren")

