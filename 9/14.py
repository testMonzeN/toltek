MIN = 10 ** 100
for x in range(0, 2030):
    k = 0
    p = 14 ** 230 + 14 ** 30 - x

    while p > 0:
        if p % 14 == 0:
            k += 1

        p //= 14

    MIN = min(MIN, k)

print(MIN)