with open('26.txt') as file:
    string = file.readline().split()
    req = int(string[0])
    mesta = int(string[1])

    text = file.readlines()

balls_count = {}
balls = []
l = []
l2 = []
for el in text:
    ID, ex1, ex2, ex3, res_sub = map(int, el.split())

    sum_ex = ex1 + ex2 + ex3
    if sum_ex not in balls:
        balls.append(sum_ex)
        
    try:
        balls_count[f'{sum_ex}'] += 1
    except:
        balls_count[f'{sum_ex}'] = 1
    l.append([ID, sum_ex, res_sub])
    l2.append([ID, sum_ex, res_sub])
    
l = sorted(l, key=lambda x: x[1], reverse=True)
balls.sort(reverse=True)

mesta1 = mesta
for ball in balls:
    mesta1 = mesta1 - balls_count[f'{ball}']

    if mesta1 <= 0:
        prohodnoi = balls[balls.index(ball) - 1]
        polu_prohodnoy = ball
        break

for i in range(req - 1, -1, -1):
    if l2[i][1] == prohodnoi:
        print(l2[i])
        res1 = l2[i][0]
        

print(res1, balls_count[f'{polu_prohodnoy}'])
