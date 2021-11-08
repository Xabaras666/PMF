from time import sleep
for hours in range (24):
    for minutes in range(60):
        for seconds in range (60):
            sleep(1)
            print (hours, ':', minutes, ':', seconds)