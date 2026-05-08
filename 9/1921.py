def f(s, k, m):
    if s + k >= 124:
        return m % 2 == 0

    if m == 0:
        return 0

    h = [f(s + 1, k, m - 1), f(s, k + 1, m - 1), f(s * 2, k, m - 1), f(s, k * 2, m - 1)]

    if (m - 1) % 2 == 0:
        return any(h)
    else:
        return any(h)

print([k for k in range(1, 113) if not(f(11, k, 1)) and f(11, k, 2)])
print([k for k in range(1, 113) if not(f(11, k, 1)) and f(11, k, 3)])
print([k for k in range(1, 113) if not(f(11, k, 2)) and f(11, k, 4)])