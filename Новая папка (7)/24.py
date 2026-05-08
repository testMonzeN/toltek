with open('24.txt') as file:
    text = file.readline().strip()

alf = '0123456789AB'
left = 0
MAX = 0
flag = False
db = {}

size = len(text)
for right in range(size):
    if text[right] in alf and flag == False and text[right] != '0':
        left = right                
        flag = True

    if flag == True:
        if text[right] not in alf:
           
            if int(text[left:right], 12) % 9 == 0:
                MAX = max(MAX, len(text[left:right]))
                try:
                    if int(text[left:right], 12) < int(db[len(text[left:right])], 12):
                        db[len(text[left:right])] = text[left:right]
                except:
                    db[len(text[left:right])] = text[left:right]

            left = right
            flag = False
            summ = 0

        if text[right] in alf:
            if int(text[left:right + 1], 12) % 9 == 0:
                MAX = max(MAX, len(text[left:right + 1]))
                try:
                    if int(text[left:right + 1], 12) < int(db[len(text[left:right + 1])], 12):
                        db[len(text[left:right + 1])] = text[left:right + 1]
                except:
                    db[len(text[left:right + 1])] = text[left:right + 1]
        

print(db[MAX])
for el in range(size - MAX - 1):
    if text[el:el + MAX] == db[MAX]:
        print(el + MAX - 1)
    
