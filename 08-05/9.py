k = 0
with open('9.txt') as file:
    for line in file:
        line = list(map(int, line.split()))

        ok1 = True
        ok2 = False

        for el in range(5):
            if line[el] < line[el + 1]:
                ok1 = False
                break

        line.sort()
        l = []
        for el in line:
            if el not in l:
                l.append(el)
        if l[-1] + l[-2] > sum(line) - l[-1] - l[-2]:
            ok2 = True

        if ok1 == True and ok2 == True:
            k += 1

print(k)


