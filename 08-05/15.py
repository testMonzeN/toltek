def DEL(x, y):
    return x % y == 0

for A in range(1, 100000):
    ok = True
    for x in range(1,  1000):
        if (x & 57 == 0 or (not(DEL(x, A)) or not(48 <= x <= 94))) == 0:
            ok = False
            break

    if ok:
        print(A)