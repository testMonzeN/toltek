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

with open('27-85a.txt', mode='r') as file:
    cluster1 = []
    cluster2 = []
    file.readline()

    for i in file:
        line = i.replace(',', '.')
        x, y = map(float, line.split())

        if -2 <= x <= 4 and 6 <= y <= 12:
            cluster1.append([x, y])
        
        if 7 <= x <= 12 and -2 <= y <= 2:
            cluster2.append([x, y])


print(len(cluster1) + len(cluster2) )
xA1, yA1 = f(cluster1, cluster2)
xB1, yB1 = f(cluster2, cluster1)
print((xA1 + xB1) / 2 * 10000, (yA1 + yB1) / 2 * 10000)


# 51428 45632
# 28289 38015