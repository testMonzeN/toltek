def f(cluster):
    k, res = 0, 0
    for A in range(len(cluster) - 1):
        for B in range(A + 1, len(cluster)):
            x1, y1 = cluster[A]
            x2, y2 = cluster[B]

            res += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            k += 1
    return res / k


with open('27B.txt', mode='r') as file:
    cluster1 = []
    cluster2 = []
    cluster3 = []
    cluster4 = []
    cluster5 = []
    cluster6 = []
    cluster7 = []
    file.readline()
    for i in file:
        line = i.replace(',', '.')
        x, y = map(float, line.split())

        if -9 <= x < -4 and -4 < y < 2:
            cluster1.append([x, y])

        if -4 < x < 1 and -2 < y < 3:
            cluster2.append([x, y])

        if -4 < x <= 1 and -10 <= y <= -4:
            cluster3.append([x, y])

        if 1 <= x <= 6 and 1 <= y <= 6:
            cluster4.append([x, y])

        if 1 <= x <= 6 and -4 <= y <= 1:
            cluster5.append([x, y])

        if 6 < x < 11 and 3 < y < 8:
            cluster6.append([x, y])

        if 6 <= x <= 11 and -6 <= y <= -1:
            cluster7.append([x, y])








res1 = f(cluster1)
res2 = f(cluster2)
res3 = f(cluster3)
res4 = f(cluster4)
res5 = f(cluster5)
res6 = f(cluster6)
res7 = f(cluster7)

print(min(res1, res2, res3, res4, res5, res6, res7) * 100000, max(res1, res2, res3, res4, res5, res6, res7) * 100000)