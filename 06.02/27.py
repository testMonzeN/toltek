with open('27-B.txt') as file:
    file.readline()

    cluster1x = []
    cluster1y = []

    cluster2x = []
    cluster2y = []

    cluster3x = []
    cluster3y = []
    for i in file:
        i = i.replace(',', '.')
        x, y = map(float, i.split())

        if -1 <= x <= 3 and 0 <= y <= 6:
            cluster1x.append(x)
            cluster1y.append(y)
        
        if -1 <= x <= 3 and 7 <= y <= 12:
            cluster2x.append(x)
            cluster2y.append(y)
        
        if 5 <= x <= 9 and -4 <= y <= 2:
            cluster3x.append(x)
            cluster3y.append(y)
        


cluster1x.sort()
cluster1y.sort()

cluster2x.sort()
cluster2y.sort()

cluster3x.sort()
cluster3y.sort()

size1x = len(cluster1x)
size1y = len(cluster1y)

size2x = len(cluster2y)
size2y = len(cluster2y)

size3x = len(cluster3x)
size3y = len(cluster3y)


x_m_1 = cluster1x[size1x // 2]
y_m_1 = cluster1y[size1y // 2]

x_m_2 = cluster2x[size2x // 2]
y_m_2 = cluster2y[size2y // 2]

x_m_3 = cluster3x[size3x // 2]
y_m_3 = cluster3y[size3y // 2]

print((x_m_1 + x_m_2 + x_m_3) / 3 * 10000, (y_m_1 + y_m_2 + y_m_3) / 3 * 10000)


# 40893 1596
# 30438 42851