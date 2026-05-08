with open('27-B.txt') as file:
    cluster1 = []
    cluster2 = []
    cluster3 = []
    x1, y1, x2, y2, x3, y3 = 0, 0, 0, 0, 0, 0
    for i in file:
        x, y = map(float, i.replace(',', '.').split())      

        if 0 <= x <= 4 and 0 <= y <= 5:
            x1 += x
            y1 += y
            cluster1.append([x, y])
            
        if 5 <= x <= 9 and 4 <= y <= 8:
            x2 += x
            y2 += y
            cluster2.append([x, y])

        if 0 <= x <= 4 and 7 <= y <= 12:
            x3 += x
            y3 += y
            cluster3.append([x, y])
        

x_sr1 = x1 / len(cluster1)
y_sr1 = y1 / len(cluster1)

x_sr2 = x2 / len(cluster2)
y_sr2 = y2 / len(cluster2)

x_sr3 = x3 / len(cluster3)
y_sr3 = y3 / len(cluster3)
print((x_sr1 + x_sr2 + x_sr3) / 3 * 10000, (y_sr1 + y_sr2 + y_sr3) / 3 * 10000)
# 31178 46663
