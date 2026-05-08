with open('26.txt') as file:
    N = int(file.readline())
    text = file.readlines()


l = []
for x in text:
    if int(x) not in l:
        l.append(int(x))
#l.sort(reverse=True)


db = {}
MAX = 0
size = len(l)
for i in range(size - 1):
    k = [l[i]]
    for j in range(i + 1, size):
        if k[-1] - l[j] >= 9:
            k.append(l[j])

    MAX = max(MAX, len(k))
    try:
        db[len(k)].append(min(k))
    except:
        db[len(k)] = []
        db[len(k)].append(min(k))

print(MAX, max(db[MAX]))

