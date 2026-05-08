with open('26/26.txt', mode='r') as file:
    size = int(file.readline())
    balls = list(map(int, file.readline().split())) # [100, 10]
    text = file.readlines()

l = [] # id, SUMM, Shtraf, kpass 
for line in text:
    SUMM = 0
    Shtraf = 0
    kpass = 0
    k = 0

    line = line.split()
    ID = int(line[0])
    for el in line[1::]:
        if el == '1':
            SUMM += balls[k]
            k += 1
        elif el == '-1':
            Shtraf += balls[k]
            SUMM -= balls[k]
            k += 1
        elif el == '0':
            kpass += 1
            k += 1
    
    l.append([ID, SUMM, Shtraf, kpass])

for i in range(size - 1):
    for j in range(i, size):
        ID = 0
        SUMM = 1
        Shtraf = 2
        kpass = 3

        if l[i][SUMM] < l[j][SUMM]:
            l[i], l[j] = l[j], l[i]

        elif l[i][SUMM] == l[j][SUMM]:
            if l[i][Shtraf] > l[j][Shtraf]:
                l[i], l[j] = l[j], l[i]
        
            elif l[i][Shtraf] == l[j][Shtraf]:
                if l[i][kpass] > l[j][kpass]:
                    l[i], l[j] = l[j], l[i]
                
                elif l[i][kpass] == l[j][kpass]:
                    if l[i][ID] > l[j][ID]:
                        l[i], l[j] = l[j], l[i]

print(l)
with open('26/111.txt', mode='a') as f:
    for line in l:
        ID, SUMM, Shtraf, kpass = line
        f.write(f'{ID} {SUMM} {Shtraf} {kpass}\n')

print(1)
'''
check = l[1002]
MAX = 0 
res1 = 0
k = 1
for el in l[len(l) // 4:]:
    if MAX < el[1]:
        res1 = el[0]
    if el[1] == check[1] and el[2] == check[2] and el[3] == check[3]:
        k += 1

print(res1, k)
'''