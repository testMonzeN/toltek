def center(cluster):
    MIN = 10 ** 100
    x_c, y_c = 0, 0
    for A in range(len(cluster)):
        res = 0
        for B in range(len(cluster)):
            x1, y1 = cluster[A]
            x2, y2 = cluster[B]
            res += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

        if res < MIN:
            MIN = res
            x_c, y_c = cluster[A]

    return [x_c, y_c]

def R(cluster, x_c, y_c):
    MAX = 0
    for A in range(len(cluster)):
        x, y = cluster[A]
        res = ((x - x_c) ** 2 + (y - y_c) ** 2) ** 0.5

        if res > MAX:
            MAX = res

    return MAX


with open("B.txt", mode='r') as file:
    cluster1 = []
    cluster2 = []
    cluster3 = []
    cluster4 = []
    for line in file:
        line = line.replace(',', '.')
        x, y = map(float, line.split())

        if 0 <= x <= 6.2 and 2.7 <= y <= 6.8:
            cluster1.append([x, y])

        elif 5.8 <= x <= 9.5 and -1 <= y <= 3.2:
            cluster2.append([x, y])

        elif 4.6 <= x <= 10.4 and 6.8 <= y <= 20:
            cluster3.append([x, y])

        elif 9.1 <= x <= 18 and 2.6 <= y <= 6.8:
            cluster4.append([x, y])


center1 = center(cluster1)
R1 = R(cluster1, x_c=center1[0], y_c=center1[1])

center2 = center(cluster2)
R2 = R(cluster2, x_c=center2[0], y_c=center2[1])

center3 = center(cluster3)
R3 = R(cluster3, x_c=center3[0], y_c=center3[1])

center4 = center(cluster4)
R4 = R(cluster4, x_c=center4[0], y_c=center4[1])

print((R1 + R2 + R3 + R4) / 4 * 10000)
