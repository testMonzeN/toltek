def f(n):
    N = n
    n = bin(n)[2:]

    if N % 6 == 0:
        n = n + n[-3] + n[-2] + n[-1]
    else:
        r = bin((N % 6) * 3)[2:]
        n = n + r

    return int(n, 2)

for N in range(10_000):
    try:
        if f(N) < 500:
            print(N)
    except:
        pass