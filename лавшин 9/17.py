def f(x, y):
    if x > 0 and y < 0:
        return True
    if x < 0 and y > 0:
        return True

    return False

l = []
count_7 = 0
with open('17 (1).txt') as file:
    for el in file:
        l.append(int(el))


for el in l:
    if abs(el) % 10 == 7:
        count_7 += 1

size = len(l)
k = 0
MAX = 0
for el in range(size - 1):
    if f(l[el], l[el + 1]):
        if l[el] + l[el + 1] < count_7:
            k += 1
            MAX = max(MAX, l[el] + l[el + 1])

print(k, MAX)