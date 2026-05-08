p = 13 ** 1402 + 11 ** 501 - 12 ** 51 - 2323
r = []
while p > 0:
    r.append(p % 27)

    p //= 27

k = 0
r.reverse()
for el in r:
    if el > 9 and el <= 20:
        k += 1
print(k)

#ArchangelPRincess1111