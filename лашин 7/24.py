with open('24_26940 (1).txt') as file:
    text = file.readline().strip()

size = len(text)
MAX = 1

for i in range(size - 1):
    for j in range(i + MAX, size):
        string = text[i:j + 1]
        if text[i] != '0':
            if string.count('0') + string.count('1') + string.count('2') + string.count('3') + string.count('4') + string.count('5') + string.count('6') + string.count('7') + string.count('8') + string.count('9') + string.count('?') <= 100:
                MAX = max(MAX, len(string))
            else:
                break
        else:
            break
print(MAX)
