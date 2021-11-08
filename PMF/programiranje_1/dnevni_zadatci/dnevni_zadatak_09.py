#Napisati program koji traži da se sa tastature unesu dva vremenska trenutka,u satima, minutama i 
# sekundama. Program racuna i ispisuje vrijeme koje je proteklo izmedju ta dva vremenska perioda.  
# Ispis treba takodjer biti u satima, minutama i sekundama.  
# Pretpostaviti da je drugi vremenski period uvijek nakon prvog.

sati_1 = int(input("Unesite vrijeme 1 h:"))
minute_1 = int(input("Unesite vrijeme 1 min:"))
sekunde_1 = int(input("Unesite vrijeme 1 sec:"))

sekunde_1_total = sekunde_1 + (minute_1 * 60) + (sati_1 * 3600)
#print (sekunde_1_total)

sati_2 = int(input("Unesite vrijeme 2 h: "))
minute_2 = int(input("Unesite vrijeme 2 min: "))
sekunde_2 = int(input("Unesite vrijeme 2 sec: "))

sekunde_2_total = sekunde_2 + (minute_2 * 60) + (sati_2 * 3600)

protekle_sekunde = sekunde_2_total - sekunde_1_total

sati_3 = protekle_sekunde // 3600
minute_3 = (protekle_sekunde // 60) % 60
sekunde_3 = protekle_sekunde % 60

print (f"Proteklo vrijeme je: {sati_3} : {minute_3} : {sekunde_3}")