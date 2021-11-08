n = int(input("Unesite broj: "))

if 9999 < n < 100000:
    e = n % 10
    n = n // 10
    d = n % 10
    n = n // 10
    c = n % 10
    n = n // 10
    b = n % 10
    n = n // 10
    a = n

    mini = min(a, b, c, d, e)

    if a == max(a, b, c, d, e):
        druga = max(b, c, d, e)
    elif b == max(a, b, c, d, e):
        druga = max(a, c, d, e)
    elif c == max(a, b, c, d, e):
        druga = max(a, b, d, e)
    elif d == max(a, b, c, d, e):
        druga = max(a, b, c, e)
    elif e == max(a, b, c, d, e):
        druga = max(a, b, c, d)

    print(f"Razlika druge najvece {druga} i najmanje {mini} je {druga - mini}")
else:
    print("Unos nije ispravan")
