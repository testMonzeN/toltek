k = 0
with open('9.txt', mode='r') as file:
    for line in file:
        count = []

        l_pov = []
        l_not_pov = []

        line = line.split()

        for el in line:
            count.append(line.count(el))
            if line.count(el) == 1:
                l_not_pov.append(int(el))
            else:
                l_pov.append(int(el))

        if sum(count) == 11:
            if min(l_pov) > min(l_not_pov):
                k += 1

print(k)
