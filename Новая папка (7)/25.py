d = [2]

start = 6651220
for check in range(3, 10000, 2):
    ok = True
    for j in range(2, check // 2 + 1):
        if check % j == 0 or str(check).count('2') != 1 or check % 5 == 0:
            ok = False
            break

    if ok:
        d.append(check)

print(1111)
size = len(d)
res_d = {}
res = []
for i in range(size - 1):
    for j in range(i, size):
        if d[i] * d[j] >= start:
            res.append(d[i] * d[j])
            res_d[d[i] * d[j]] = max(d[i], d[j])

res.sort()
print(res[:5])
