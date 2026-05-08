with open('24 (2).txt') as file:
    text = file.readline().strip()


left = 0
count = 0
size = len(text)
alf = '0123456789ABCDEF'
for right in range(size):
    if text[right] in alf and text[left] != '0' and text[left] in alf:
        if text[left:right + 1].count('9') + text[left:right + 1].count('A') + text[left:right + 1].count('B') + text[left:right + 1].count('C') + text[left:right + 1].count('D') + text[left:right + 1].count('E') + text[left:right + 1].count('F') >= 12:
            count += 1

    if text[right] not in alf:
        while left <= right - 1:
            left += 1
            count += 1



    while text[left] not in alf:
        left += 1

print(count)
