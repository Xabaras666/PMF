a = 5.4 + 0.2
if 5.6 == a:
    print("Jednaki")
else:
    print("Nisu")

if 5.6 - a < 0.0000000001 and a - 5.6 < 0.0000000001:
    print("Jednaki")
else:
    print("Nisu")
