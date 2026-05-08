with open('26-test.txt') as file:
    size = int(file.readline())

    req = file.readlines()

db = {}
for el in req:
    nomer, summa, clas = map(int, el.split())

    try:
        db[str(clas)][0][str(nomer)] += summa
    except:
        try: db[str(clas)].append({str(nomer): summa})
        except:
            db[str(clas)] = []
            db[str(clas)].append({str(nomer): summa})
    
         

MAX = 0
for clas_car in db:
    for ID in db[clas_car]:
        for nomer in ID:
            MAX = max(ID[nomer], MAX)
        
for clas_car in db:
    for ID in db[clas_car]:
        for nomer in ID:
            if ID[nomer] == MAX:
                print(ID, clas_car)


