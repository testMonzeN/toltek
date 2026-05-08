l = []
req = []
with open('26-20.txt', mode='r') as file:
    size = int(file.readline())
    for line in file:
        a1, a2 = map(int, line.split())
        l.append(a1)
        l.append(a2)

        req.append([a1, a2, True])

l.sort()
shleifovka = []
pokraska = []
res1 = 0
for el in l:
    for elREQ in range(len(req)):
        if el in req[elREQ] and req[elREQ][2] == True:
            if el == req[elREQ][0]:
                shleifovka.append(elREQ + 1)
                res1 = elREQ + 1
                req[elREQ][2] = False

            if el == req[elREQ][1]:
                pokraska.append(elREQ + 1)
                pokraska.reverse()
                res1 = elREQ + 1
                req[elREQ][2] = False




shleifovka_and_pokraska = []
for el in shleifovka:
    shleifovka_and_pokraska.append(el)

for el in pokraska:
    shleifovka_and_pokraska.append(el)


print(res1, shleifovka_and_pokraska.index(res1))


