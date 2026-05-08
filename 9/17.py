def f(x, y, z):
    k = 0

    if 1000 <= abs(x) <= 9999:
        k += 1
    if 1000 <= abs(y) <= 9999:
        k += 1
    if 1000 <= abs(z) <= 9999:
        k += 1

    return k <= 2

l = []
a = []
with open('17 (2).txt', mode='r') as file:
    for el in file:
        l.append(int(el))

for el in l:
    if abs(el) % 100 == 45:
        a.append(el)
size = len(l)
k = 0
MAX = 0
for el in range(size - 2):
    if f(l[el], l[el + 1], l[el + 2]):
        if l[el] + l[el + 1] + l[el + 2] <= max(a):
            k += 1
            MAX = max(MAX, l[el] + l[el + 1] + l[el + 2])

print(k, MAX)