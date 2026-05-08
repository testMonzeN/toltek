with open('24.txt') as file:
    text = file.readline().strip()

left = 0
MAX = 0
db = {}
size = len(text)
flag = False


for right in range(size):
    if text[right] in '123456789ABCDE' and flag == False:
        flag = True
        left = right

    if flag:
        if text[right] in '0123456789ABCDE':
            if int(text[left:right + 1], 15) % 5 == 0:
                MAX = max(MAX, int(text[left:right + 1], 15))
                db[int(text[left:right + 1], 15)] = text[left:right + 1]
        else:
            flag = False
            for left2 in range(left, right - 2):
                for right2 in range(left2 + 1, right - 1):
                    if int(text[left2:right2 + 1], 15) % 5 == 0:
                        MAX = max(MAX, int(text[left2:right2 + 1], 15))
                        db[int(text[left2:right2 + 1], 15)] = text[left2:right2 + 1]

print(db[MAX])
# E2B7450450937681206413258079070926134580762180493504983671520053791264080395462810706739412850061592348700437D15: 13381