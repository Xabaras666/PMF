m = 2 ** 31
a = 1103515245
c = 12345

def rand(seed):
    seed = (a * seed + c) % m;
    return seed

seed = 15
for _ in range(20):
    seed = rand(seed)
    print(seed)