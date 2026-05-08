f = {}
g = {}
q = {}

for n in range(250_000, -1000, -1):
    if n < 210_000:
        q[n] = q[n + 3] + 2
    else:
        q[n] = n + 4

for n in range(-500, 200_000):
    if n < 11:
        g[n] = q[n] + 6
    else:
        g[n] = g[n - 3] + 5

for n in range(200_000, 0, -1):
    if n < 4300:
        f[n] = f[n + 2] + 2
    else:
        f[n] = g[n - 3]

print(f[1])
