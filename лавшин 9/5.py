def f(n):
    R = bin(n)[2:]
    if n % 2 == 0:
        if len(R) >= 3:
            R2 = R + R[-3] + R[-2] + R[-1]
        elif len(R) == 2:
            R2 = R + '0' + R[-2] + R[-1]
        elif len(R) == 1:
            R2 = R + '0' + '0' + R[-1]
    else:
        R2 = '1' + R + '01'

    return int(R2, 2)

print(f(5))

for N in range(1, 10000):
    if 100 <= f(N) <= 200:
        print(N, f(N), abs(155 - f(N)))