with open('tezt-24.txt') as file:
    text = file.readline().strip()
#text = '10(5(4)4(10))'


count = 0
size = len(text)
left = 0

status = False
l = []
for right in range(size):
    if text[right] == '(' or text[right] == ')':
        if len(text[left:right]) == 0:
            l.append('0')
        else:
            l.append(text[left:right])

        l.append(text[right])
        left = right + 1

l2 = []
el = 0
while el <= len(l) - 3:
    if l[el] == '(' and l[el + 2] == ')':
        l2.append(l[el])
        l2.append(l[el + 2])
        el += 3
    try:
        l2.append(int(l[el]))
    except:
        l2.append(l[el])

    el += 1

l2.append(2)
l2.append('(')
l2.append(43)


count = 0
size = len(l2)
left = 0

status = False
for right in range(size):
    if l2[right] == '(' and l2[right + 1] == ')':
        left = right

        left2 = left
        right2 = right
        while left2 >= 0 and (text[left2] != ')'):

