def f(cluster):
    k, res = 0, 0
    for A in range(len(cluster) - 1):
        for B in range(A + 1, len(cluster)):
            x1, y1 = cluster[A]
            x2, y2 = cluster[B]

            res += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            k += 1
    print(k)
    return res / k


with open('27A.txt', mode='r') as file:
    cluster1 = []
    cluster2 = []
    cluster3 = []
    cluster4 = []
    file.readline()
    for i in file:
        line = i.replace(',', '.')
        x, y = map(float, line.split())

        if -3 <= x <= -0.5 and 0 <= y <= 3:
            cluster1.append([x, y])

        elif -2 <= x <= 1 and -4 <= y <= 0:
            cluster2.append([x, y])

        elif 2 <= x <= 5 and 2 <= y <= 5:
            cluster3.append([x, y])

        elif 3 <= x <= 8 and -3 <= y <= 2:
            cluster4.append([x, y])

res1 = f(cluster1)
res2 = f(cluster2)
res3 = f(cluster3)
res4 = f(cluster4)

print(len(cluster1))
print(len(cluster1) + len(cluster2) + len(cluster3) + len(cluster4))
print(res1 * 100000, res2 * 100000, res3 * 100000, res4 * 100000)
print(min(res1, res2, res3, res4) * 100000, max(res1, res2, res3, res4) * 100000)
print(159020 - 158994)