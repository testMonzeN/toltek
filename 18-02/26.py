l = []
balls = []
balls_db = {}
with open('26.txt') as file:
    size, mesta = map(int, file.readline().split())
    for req in file:
        ID, r1, r2, r3, rsubes = map(int, req.split())
        l.append([ID, r1 + r2 + r3, rsubes])
        if (r1 + r2 + r3) not in balls:
            balls.append(r1 + r2 + r3)
            balls.sort(reverse=True)

        try:
            balls_db[r1 + r2 + r3][0] += 1
            balls_db[r1 + r2 + r3][1] = ID
        except:
            balls_db[r1 + r2 + r3] = [1, ID]

#l = sorted(l, key=lambda y:y[1], reverse=True)

# Из числа кандидатов, набравших полупроходной балл, на имеющиеся места принимаются кандидаты, имеющие более высокий балл за собеседование,
#                                                       а при равенстве баллов за собеседование – приоритет имеют кандидаты с наименьшими ID
for i in range(size - 1):
    for j in range(size):
        ID, ball, rsubes = 0, 1, 2
        if l[i][ball] < l[j][ball]:
            l[i], l[j] = l[j], l[i]
        elif l[i][ball] == l[j][ball]:
            if l[i][rsubes] < l[j][rsubes]:
                l[i], l[j] = l[j], l[i]
            elif l[i][rsubes] == l[j][rsubes]:
                if l[i][ID] > l[j][ID]:
                    l[i], l[j] = l[j], l[i]

r = 0
for i in range(len(balls)):
    mesta -= balls_db[balls[i]][0]
    if mesta <= 0:
        r = balls[i - 1]
        print(balls_db[balls[i - 1]][1], balls_db[balls[i]][0])
        break

for i in l:
    ID, ball, rsubes = i
    if ball == r:
        print(ID, ball, rsubes)