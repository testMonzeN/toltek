def f(n):
    d = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 2 != 0 and i not in d:
                d.append(i)
            if (n // i) % 2 != 0 and (n // i) not in d:
                d.append(n // i)
    
    if d:
        if len(d) >= 5:
            d.sort()
            return [d[-5], len(d)]
        else:
            return []
    else:
        return []


for x in range(300_000_000 - 1, 299_999_500, -1):
    if f(x):
        print(f(x))


