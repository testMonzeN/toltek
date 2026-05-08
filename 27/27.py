def f(cluster1, cluster2):
    xk, yk, MIN = 0, 0, 10*100
    for A in range(len(cluster1)):
        for B in range(len(cluster2)):
            x1, y1 = cluster1[A]
            x2, y2 = cluster2[B]
            d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            if d < MIN:
                MIN = d 
                xk = x1
                yk = y1

    return xk, yk

with open('27-85b.txt', mode='r') as file:
    cluster1 = []
    cluster2 = []
    cluster3 = []
    file.readline()

    for i in file:
        line = i.replace(',', '.')
        x, y = map(float, line.split())

        if -2 <= x <= 2 and 0 <= y <= 4:
            cluster1.append([x, y])
        
        if 3 <= x <= 7 and 1 <= y <= 5:
            cluster2.append([x, y])

        if 2 <= x <= 5 and 6 <= y <= 9:
            cluster3.append([x, y])

#print(len(cluster1) + len(cluster2) + len(cluster3))
xA1, yA1 = f(cluster1, cluster2)
xA2, yA2 = f(cluster1, cluster3)

xB1, yB1 = f(cluster2, cluster1)
xB2, yB2 = f(cluster2, cluster3)

xC1, yC1 = f(cluster3, cluster1)
xC2, yC2 = f(cluster3, cluster2)


print((xA1 + xA2 + xB1 + xB2 + xC1 + xC2) / 6 * 10000, (yA1 + yA2 + yB1 + yB2 + yC1 + yC2) / 6 * 10000)

# 22330 75744
# 28289 38015