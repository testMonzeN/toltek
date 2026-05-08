def f(x, y, z):
    k = 0
    if 1 <= x:
        k += 1

    if 1 <= y:
        k += 1

    if 1 <= z:
        k += 1

    return k >= 1


def f2(x, y, z):
    global MINN
    sr = (x + y + z) / 3
    return (sr < 0 and sr > MINN)

l = []
a = []
with open('17 (3).txt') as file:
    for i in file:
        l.append(int(i))

for i in l:
    if abs(i) % 100 == 33:
        a.append(i)

MINN = min(a)
size = len(l)

cnt = 0
MAX = -1 * (10 ** 13)
for el in range(size - 2):
    if f(l[el], l[el + 1], l[el + 2]):
        if f2(l[el], l[el + 1], l[el + 2]):
            cnt += 1
            MAX = max(MAX, sum([l[el], l[el + 1], l[el + 2]]))

print(cnt, MAX)