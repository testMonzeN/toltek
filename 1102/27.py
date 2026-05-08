def f(cluster):
    sr = 0
    k = 0
    for A in range(len(cluster)):
        for B in range(len(cluster)):
            x1, y1 = cluster[A]
            x2, y2 = cluster[B]
            d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

            if d < 1:
                k += 1
        #sr += k / len(cluster)
    return k / len(cluster)

with open('27-A2.txt') as file:
    cluster1 = []
    cluster2 = []
    cluster3 = []
    cluster4 = []
    file.readline()
    for line in file:
        line = line.replace(',', '.')
        x, y = map(float, line.split())
        if -2 <= x <= 0 and 0 <= y <= 3:
            cluster1.append([x, y])

        if -2 <= x <= 1 and -4 <= y <= 0:
            cluster2.append([x, y])

        if 2 <= x <= 5 and 2 <= y <= 5:
            cluster3.append([x, y])

        if 4 <= x <= 8 and -3 <= y <= 2:
            cluster4.append([x, y])

sr1 = f(cluster1)
sr2 = f(cluster2)
sr3 = f(cluster3)
sr4 = f(cluster4)
print(min(sr1, sr2, sr3, sr4) * 100_000, (sr1 + sr2 + sr3 + sr4) / 4 * 100000)


# 100813 101652
# 23982 47539
