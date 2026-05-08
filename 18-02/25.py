from fnmatch import fnmatch

def f(x):
    s = 0
    for i in str(x):
        s += int(i)
    return s

l = []
for num in range(0, 10**9 + 1, 7863):
    if fnmatch(str(num), '?54*32*1'):
        l.append([f(num), num])

size = len(l)
# TODO Отсортируйте числа в порядке возрастания суммы цифр, а при одинаковой сумме цифр – по возрастанию самого числа.
for i in range(size):
    for j in range(size):
        SUMM = 0
        NUMBER = 1
        if l[i][SUMM] < l[j][SUMM]:
            l[i], l[j] = l[j], l[i]

        elif l[i][SUMM] == l[j][SUMM]:
            if l[i][NUMBER] < l[j][NUMBER]:
                l[i], l[j] = l[j], l[i]

for i in l:
    r1, r2 = i
    print(r2, r1)