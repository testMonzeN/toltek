import itertools

k = 0
for x in itertools.product('БОТАЙ', repeat=6):
    c = ''.join(x)


    if 'ЙОЙО' not in c:
        k += 1

print(k)
