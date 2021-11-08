x = int(input("Unesite trocifren broj: "))

# Izdvojimo cifre a, b i c
c = x % 10

x = x // 10
b = x % 10

x = x // 10
a = x

if a + 1 == b or b + 1 == a:
    print("Dobar")
elif a + 1 == c or c + 1 == a:
    print("Dobar")
elif b + 1 == c or c + 1 == b:
    print("Dobar")
else:
    print("Nije dobar")
