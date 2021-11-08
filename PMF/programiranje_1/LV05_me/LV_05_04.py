n = int(input())

if n <= 0:
    print("Morate unijeti prirodan broj.")
else:
    max_cifra = 0           # 0 je sto posto najmanja moguca cifra tako da cemo je zamijeniti sa vecom
    while n > 0:
        trenutna_cifra = n % 10
        if max_cifra < trenutna_cifra:
            max_cifra = trenutna_cifra

        n = n // 10

    print('Najveca cifra je:', max_cifra)