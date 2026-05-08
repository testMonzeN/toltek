def f(x, y):
    k = 0
    if 100 <= x <= 999:
        k += 1

    if 100 <= y <= 999:
        k += 1

    return k == 1

l = []
a = []
with open('17.txt') as file:
    for el in file:
        l.append(int(el))

for el in l:
    if len(str(el)) == 2:
        if str(el)[-1] == '3':
            a.append(int(el))

size = len(l)
MIN = 10 ** 10
count = 0
for el in range(size - 1):
    if f(l[el], l[el + 1]):
        if str(l[el])[0] in '2468' and str(l[el + 1])[0] in '2468':
            if sum([l[el], l[el + 1]]) % max(a) == 0:
                count += 1
                MIN = min(MIN, sum([l[el], l[el + 1]]))

print(count, MIN)