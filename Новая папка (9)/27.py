# 164
# 900
with open('27-164b.txt') as file:
    size, K = map(int, file.readline().split())
    text = file.readlines()

MAX = 0
l = []
for el in text:
    a1, a2, a3 = map(int, el.split())
    l.append([a1, a2, a3])

l = sorted(l, key=lambda y:y[0])
for i in range(size - 1):
    for j in range(i + 1, size):
        if abs(l[i][1] - l[j][1]) >= K:
            MAX = max(MAX, abs(l[i][2] - l[j][2]))
        
print(MAX)
