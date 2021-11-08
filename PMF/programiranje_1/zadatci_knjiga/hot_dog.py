ljudovi = int(input('Broj ljudi:'))
hodogvi = int (input('Broj hot dogova po osobi: '))

hot_dog_pack = 10
bun_pack = 8

min_hot_dog = ljudovi * hodogvi
min_bun = ljudovi * hodogvi

min_hot_dog_pack = min_hot_dog // 10
min_bun_pack = min_bun // 8
print (min_hot_dog_pack, min_bun_pack)

hot_dog_leftover = min_hot_dog % 10
bun_leftover = min % 8
print (hot_dog_leftover, bun_leftover)