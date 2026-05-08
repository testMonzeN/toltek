with open('24_24613.txt', mode='r') as file:
    text = file.readline().strip()


count = 0
left = 0
size = len(text)
for right in range(size):
    if text[left:right + 1].count('HALLOWEEN') == 5 and text[left:right + 1].count('TRICK') == 5 and text[left:right + 1].count('TREAT') == 5:
        left2 = left
        while text[left2:right + 1].count('HALLOWEEN') == 5 and text[left2:right + 1].count('TRICK') == 5 and text[left2:right + 1].count('TREAT') == 5:
            count += 1
            left2 += 1



    else:
        while text[left:right + 1].count('HALLOWEEN') > 5 or text[left:right + 1].count('TRICK') > 5 or text[left:right + 1].count('TREAT') > 5:
            left += 1

print(count)
