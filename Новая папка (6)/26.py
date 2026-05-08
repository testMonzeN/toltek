with open('26.txt') as file:
    N = file.readline()
    text = file.readlines()

l = []
for x in text:
    if int(x) not in l:
        l.append(int(x))
        
l.sort(reverse=True)
res = [l[0]]
for i in range(len(l)):
    if res[-1] - l[i] >= 7:
        res.append(l[i])

print(1, len(res), res[-1])
    
