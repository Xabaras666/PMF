n = int(input())

k = n -1
for i in range(0, n):
    for j in range(0, k):
        print(end= ' ')

    k -= 1
    for j in range(0, i + 1):
        if j == 0 or i == j:
            print('*', end=' ')
        else:
            print(' ', end= ' ')

    print()
for i in range(0, n):
    for j in range(0, n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print('*', end =' ')
        else:
            print(' ', end= ' ')
    
    print()