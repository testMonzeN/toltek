def is_prime(x):
    x = abs(x)
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False

    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False

    return True


def f(x):
    X = x
    x = abs(x)
    divs = []
    for d in range(2, x):
        while x % d == 0:
            if is_prime(d):
                x //= d
                divs.append(d)

            if len(divs) == 10:
                break

        if len(divs) == 10:
            break

    if divs:
        s = 1
        for d2 in divs:
            s *= d2

        if is_prime(X // s):
            divs.append(X // s)

    if len(divs) == 11:
        return divs
    else:
        return []

l = []
for check in range(999680, 0, -2):
    if f(check):
        print(check, max(f(check)))
        l.append([check, max(f(check))])

l = sorted(l, key=lambda y:y[1], reverse=True)
print(l)


984576 641
987648 643
993792 647
990208 967
994304 971






