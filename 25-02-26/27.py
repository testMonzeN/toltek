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


with open("A.txt", mode='r') as file:
    cluster1 = []
    cluster2 = []
    file.readline()
    for line in file:
        line = line.replace(',', '.')
        x, y = map(float, line.split())

        if 2 <= x <= 6.5 and -2 <= y <= 2.2:
            cluster1.append([x, y])

        if 5 <= x <= 12 and 2.1 <= y <= 10:
            cluster2.append([x, y])

center1 = center(cluster1)
R1 = R(cluster1, x_c=center1[0], y_c=center1[1])

center2 = center(cluster2)
R2 = R(cluster2, x_c=center2[0], y_c=center2[1])

print((R1 + R2) / 2 * 10000)
