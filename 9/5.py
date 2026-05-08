def f(n):
    r = ''
    N = n
    while n > 0:
        r = str(n % 3) + r
        n //= 3

    if N % 3 == 0:
        r = '1' + r + '02'
    else:
        n = (N % 3) * 4
        r2 = ''
        while n > 0:
            r2 = str(n % 3) + r2
            n //= 3

        r = r + r2

    return int(r, 3)

for N in range(1000):
    if f(N) < 1234:
        print(N, f(N))