n = int(input())

brojac = 0

trenutni = 1

while brojac < n:
    trenutni += 1
    cudan = True
    kopija = trenutni
    while kopija > 0:
        if kopija % 10 != 2 and kopija % 10 != 3:
            cudan = False
        kopija //= 10
    if cudan:
        brojac += 1

print(trenutni)