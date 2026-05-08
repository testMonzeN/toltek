def f(s, k, m):
    if s + k >= 5110:
        return m % 2 == 0

    if m == 0:
        return 0

    h = [f(s + 1, 0, m - 1), f(s + 4, 0, m - 1), f(s * 2, 0, m - 1)]

    if (m - 1) % 2 == 0:
        return any(h)
    else:
        return all(h)

print([s for s in range(1, 5109 + 1) if not(f(s, 0, 1)) and f(s, 0, 2)])
print([s for s in range(1, 5109 + 1) if not(f(s, 0, 1)) and f(s, 0, 3)])
print([s for s in range(1, 5109 + 1) if not(f(s, 0, 2)) and f(s, 0, 4)])

