with open('24_26940 (1).txt') as file:
    text = file.readline().strip()

size = len(text)
MAX = 1

left = 0
for right in range(size):
    if text[left] != '0':
        if text.count('0') + text.count('1') + text.count('2') + text.count('3') + text.count('4') + text.count('5') + text.count('6') + text.count('7') + text.count('8') + text.count('9') + text.count('?') <= 100:
            MAX = max(MAX,len(text) )
