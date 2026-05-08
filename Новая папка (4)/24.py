with open('24.txt', mode='r') as file:
    text = file.read()

size = len(text)
left = 0
MAX = 0
S = 0
flag = False
for right in range(size):
    if text[right] in '02468' and flag == False:
        left = right
        flag = True
        
    elif text[right] == 'S' and flag == True:
        if S<31:
            S=S+1
        else:
            MAX = max(MAX, len(text[left:right]))
            S = 0
            flag = False
    elif text[right] in '02468' and flag == True and S == 31:
        MAX = max(MAX, len(text[left:right]))
        S = 0
        flag = False
        left = right

    elif text[right] in '02468' and flag == True and S < 31:
        S = 0
        flag = True
        left = right

print(MAX)
