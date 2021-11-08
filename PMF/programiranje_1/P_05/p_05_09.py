#!/bin/python3

import random

ulog = int(input('Ulog:'))
cilj = int(input('Cilj:'))
BROJ_SIM = 1000

br_opklada = 0
br_pobjeda = 0

for _ in range(BROJ_SIM):
  # Jedan eksperiment
  novac = ulog
  while (novac > 0) and (novac < cilj):
    # Jedna opklada.
    br_opklada += 1
    if random.randrange(0, 2) == 0:
      novac += 1
    else:
      novac -= 1
  if novac == cilj:
      br_pobjeda += 1
print(str(100 * br_pobjeda / BROJ_SIM) + '% wins')
print('Prosjecan broj opklada: ' + str(br_opklada // 
  BROJ_SIM))