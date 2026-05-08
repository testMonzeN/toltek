def f(n):
    N = n
    r = ''

    s = 0
    while n > 0:
        r = str(n % 3) + r
        s += (n % 3)
        n //= 3

    if N % 3 == 0:
        r = r + r[-3] + r[-2] + r[-1]
    else:
        s = (s * 5)
        r2 = ''
        while s > 0:
            r2 = str(s % 3) + r2
            s //= 3

        r = r2 + r

    return int(r, 3)

for N in range(10, 1000):
    R = f(N)
    if R > 1032:
        print(N, R)