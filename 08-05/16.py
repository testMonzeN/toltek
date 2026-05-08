from functools import lru_cache

@lru_cache(None)
def f(n):
    if n <= 10:
        return 42
    if n > 10:
        return f(n - 3) * n

for n in range(10, 40):
    f(n)


print(335130 * 335127 / f(20))