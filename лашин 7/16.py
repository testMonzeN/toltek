q = {}
g = {}
f = {}

# q
for n in range(40001):
    if n < 21:
        q[n] = n + 4
    if n >= 21:
        q[n] = q[n - 4] + 2

# g
for n in range(40000, 0, -1):
    if n < 11240:
        g[n] = g[n + 3] + 2
    if n >= 11240:
        g[n] = q[n]

# f
for n in range(30000):
    if n < 43:
        f[n] = g[n + 4]
    if n >= 43:
        f[n] = 2 * f[n - 2] - f[n - 4] + 2

print(f[2026])

