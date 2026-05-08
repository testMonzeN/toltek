l = []
db = {}
MAX = 0

with open('26-28.txt', mode='r') as file:
    _ = int(file.readline())
    for line in file:
        StartTime, EndTime = map(int, line.split())
        if [StartTime, EndTime] not in l:
            l.append([StartTime, EndTime + 10])
size = len(l)

for i in range(size - 1):
    for j in range(i + 1, size):
        StartTime, EndTime = 0, 1
        if l[i][EndTime] > l[j][EndTime]:
            l[i], l[j] = l[j], l[i]

i = 0
j = 0
print(len(l))
while i<len(l)-2:
    j = i+1
    while j<len(l)-1:
        if l[i][0]>=l[j][0] and l[i][1]<=l[j][1]:
            print(l[i], l[j])
            l.pop(j)
        elif  l[j][0]>=l[i][0] and l[j][1]<=l[i][1]:
            print(l[i],l[j])
            l.pop(i)
        j=j+1
    i=i+1


print(len(l))
size = len(l)
MAX = 0
for i in range(size - 1):
    m = [l[i][1]]
    m2 = [l[i]]
    for j in range(i + 1, size):
        if l[j][0] == m[-1]:
            m.append(l[j][1])
            m2.append(l[j])

    print(m2)
    MAX = max(MAX, len(m))


print(MAX)
print(l)

'''        elif l[i][StartTime] == l[j][StartTime]:
        if l[i][StartTime] > l[j][StartTime]:
                l[i], l[j] = l[j], l[i]'''

'''i = 0
while i < len(l) - 1:
    while l[i][0] == l[i + 1][0]:
        l.pop(i + 1)
        if i >= len(l)-1:
            break
    print(l[i])
    i += 1'''
'''

for i in range(size - 1):
    lMAX = 0
    StartTime, EndTime = 0, 1
    m = [l[i][EndTime]]
    for j in range(i + 1, size):
        if l[j][StartTime] - m[-1] >= 10:
            m.append(l[j][EndTime])
            lMAX = max(lMAX, m[-1] - l[j][StartTime])

    db[len(m)] = lMAX
    MAX = max(MAX, len(m))

print(MAX, db[MAX])
'''