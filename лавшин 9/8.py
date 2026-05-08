from itertools import product

k = 0
for x in product('01234', repeat=6):
    c = ''.join(x)

    if c[0] != '0':
        if c.count('3') == 2 and c.count('1') >= 2:
            k += 1
print(k)
