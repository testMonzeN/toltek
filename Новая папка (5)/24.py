with open('24.txt') as file:
    text = file.read().replace('1', ' ').replace('2', ' ').replace('3', ' ').replace('4', ' ').replace('5', ' ').replace('6', ' ').replace('7', ' ').replace('8', ' ').replace('9', ' ').replace('0', ' ')
    text = text.split()


l = []

for i in text:
    l.append(len(i))
