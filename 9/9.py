k = 0
count = 1
with open('9.txt', mode='r') as file:
    for line in file:
        line = line.split()
        line_int = []
        r1 = True
        r2 = False

        s = 0
        for el in line:
            s += int(el)
            line_int.append(int(el))
            if line.count(el) != 1:
                r1 = False

        if max(line_int) - min(line_int) > s - max(line_int) - min(line_int):
            k += 1

        if k == 50:
            print(count, line)

        count += 1