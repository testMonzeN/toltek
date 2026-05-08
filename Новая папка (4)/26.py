with open('26.txt', mode='r') as file:
    N = file.readline()
    text = file.readlines()
    

l = []
req = []

pokraska = []
shleifovka = []
res1 = 0
for el in text:
    a1, a2 = map(int, el.split())
    l.append(a1)
    l.append(a2)
    req.append([a1, a2])

l.sort()
for el in l:
    for elREQ in range(len(req)):
        if el in req[elREQ] and el == req[elREQ][0] and (elREQ + 1) not in pokraska and (elREQ + 1) not in shleifovka:
            pokraska.append(elREQ + 1)
            res1 = elREQ + 1
        elif el in req[elREQ] and el == req[elREQ][1] and (elREQ + 1) not in shleifovka and (elREQ + 1) not in pokraska:
            shleifovka.append(elREQ + 1)
            res1 = elREQ + 1
    
shleifovka.reverse()

a = []
for i in pokraska:
    a.append(i)

for i in shleifovka:
    a.append(i)

print(res1, a.index(res1))
