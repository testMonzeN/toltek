def f(x, y):
    if x < y or x == 433:
        return 0
    if x == y:
        return 1

    if x > y:
        return f(x - 5, y) + f(x - 10, y) + f(x // 3, y)

print(f(453, 323) * f(323, 213))