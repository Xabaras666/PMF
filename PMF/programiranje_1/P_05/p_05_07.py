#!/bin/python3

import random

for _ in range(4):
  novcic = random.randrange(2)
  if novcic == 0:
    print('glava', end=' ')
  else:
    print('pismo', end=' ')

print()


for _ in range(10):
  kockica = random.randint(1, 6)
  print(kockica, end=' ')