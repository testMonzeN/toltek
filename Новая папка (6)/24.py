with open('24.txt') as file:
    text = file.read()

alf = '0123456789ABCD'
left = 0
MAX = 0
flag = False
size = len(text)
for right in range(size):

    # начало числа
    if text[right] in alf and text[right] != '0' and flag == False:
        left = right
        flag = True

    if flag:
        # если я иду по содержанию подстроки
        if text[right] in alf:
            if int(text[right], 14) % 2 == 0:
                MAX = max(MAX, len(text[left:right + 1]))

        # если встретил сивол не пренадлежащий алфавиту 14 сс
        if text[right] not in alf:
            flag = False
            left = right

        
print(MAX)
