k = 1
with open('9.txt') as file:
    for line in file:
        count = []
        line_int = []
        line = line.split()

        for el in line:
            line_int.append(int(el))

        ok = True
        for el in line_int:
            if line_int.count(el) != 1:
                ok = False
                break

        if ok:
            sum1 = max(line_int) + min(line_int)
            sum2 = sum(line_int) - sum1
            if 3 * sum1 == sum2:
                print(k, line_int)

        k += 1