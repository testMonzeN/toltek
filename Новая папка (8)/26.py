db = {} # id_студента: [задача1, задача2, ...]
MAX = 0
with open('26.txt') as file:
    N = file.readline()
    text = file.readlines()

l = []
for el in text:
    a1, a2 = map(int, el.split())
    db[a1] = [0, 0]
    l.append([a1, a2])

l = sorted(l, key= lambda y: y[1])
for item in l:
    ID, zadacha = item
    
    if db[ID][0] == 0:
        db[ID][0] = zadacha
        db[ID][1] = 1
        MAX = max(MAX, db[ID][1])

    elif db[ID][0] != 0 and abs(db[ID][0] - zadacha) == 0:
        db[ID][0] = zadacha
        MAX = max(MAX, db[ID][1])

    elif db[ID][0] != 0 and abs(db[ID][0] - zadacha) == 1:
        db[ID][0] = zadacha
        db[ID][1] += 1
        MAX = max(MAX, db[ID][1])

    elif db[ID][0] != 0 and abs(db[ID][0] - zadacha) > 1:
        db[ID][0] = zadacha
        db[ID][1] = 1
        MAX = max(MAX, db[ID][1])
    
        



i = 1        
while True:
    try:
        if db[i][1] == MAX:
            print(i, MAX)
            break
    except:
        pass
    
    i += 1
    
