import random
#random.seed(42)

n = int(input())

eksperiment_uspio = 0

# idemo 10 000 eksperimenata
for i in range(100):
    
    #jedna simulacija gdje bacamo kockicu 30 puta
    broj_sestica = 0

    for j in range(10):
        #generisemo rezultat bacanja
        broj = random.randint(1, 6)

        #ako je to sestica
        if broj == 6:
            broj_sestica += 1
        else:
            broj_sestica = 0

        if broj_sestica == n:
            eksperiment_uspio += 1

        print(f"eksepriment {i} : {broj}  - sestica zaredom {broj_sestica}")

print(eksperiment_uspio / 10000)