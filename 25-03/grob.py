pars = []
l = []
res2 = 0

with open('26.txt', mode='r') as file:
    size = int(file.readline())
    for line in file:
        a1, a2 = line.split()
        l.append([int(a1), a2, False])

for podarok1 in range(len(l) - 1):
    for podarok2 in range(podarok1 + 1, len(l)):
        if l[podarok1][1] != l[podarok2][1]:
            if l[podarok1][0] + l[podarok2][0] == 2026:
                res2 += 2026
                pars.append(l[podarok1])
                pars.append(l[podarok2])
                l[podarok1][2] = True
                l[podarok2][2] = True

                break

    if l[podarok1][2] == False:
        for podarok2 in range(podarok1 + 1, len(l)):
            if l[podarok1][1] == l[podarok2][1]:
                if l[podarok1][0] + l[podarok2][0] == 2026:
                    pars.append(l[podarok1])
                    pars.append(l[podarok2])
                    l[podarok1][2] = True
                    l[podarok2][2] = True
                    break

print(len(pars), res2)