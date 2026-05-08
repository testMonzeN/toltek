with open('24 (3).txt') as file:
    text = file.readline().strip()

MAX = 1
size = len(text)
for left in range(size - 1):
    for right in range(left + MAX, size):
        if text[left:right + 1].count('18') == 3:
            if text[left:right + 1].count('A') + text[left:right + 1].count('E') + text[left:right + 1].count('I') + text[left:right + 1].count('O') + text[left:right + 1].count('U') + text[left:right + 1].count('Y') == 2:
                if text[left:right + 1][0] in 'AEOIUY' and text[left:right + 1][-1] in 'AEOIUY':
                    MAX = max(MAX, len(text[left:right + 1]))
                else:
                    break
            elif text[left:right + 1].count('A') + text[left:right + 1].count('E') + text[left:right + 1].count('I') + text[left:right + 1].count('O') + text[left:right + 1].count('U') + text[left:right + 1].count('Y') > 2:
                break
        elif text[left:right + 1].count('18') > 3:
            break

print(MAX)