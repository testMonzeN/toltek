with open('C://Users/toltek/Desktop/Roman/1102/24.txt') as file:
    text = file.readline().strip()

alf = '0123456789ABCD'
left = 0
MAX = 0
db = {}
db2 = {}
flag = False
size = len(text)
print(int('AAAAA', 14) < int('DDDA', 14))
for right in range(size):
    if text[right] in alf and flag == False and text[right] != '0':
        left = right
        flag = True

    if flag == True:
        if text[right] in alf:
            if int(text[left:right + 1], 14) % 5 == 0:
                db[int(text[left:right + 1], 14)] = text[left:right + 1]
                MAX = max(MAX, int(text[left:right + 1], 14))
        else:
            flag = False
            for left2 in range(left, right - 1):
                for right2 in range(left2 + 1, right):
                    if int(text[left2:right2], 14) % 5 == 0:
                        db[int(text[left2:right2], 14)] = text[left2:right2]
                        MAX = max(MAX, int(text[left2:right2], 14))
            
print(db[MAX])
