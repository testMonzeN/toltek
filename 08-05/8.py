import itertools

k = 1
for x in itertools.product('АЕЛПРЬ', repeat=6):
    c = ''.join(x)

    if c == 'ПАЕРЕЛ' :
        print(k, c)

    if 'АА' in c or "ЕЕ" in c or 'АЕ' in c or 'ЕА' in c:
        k += 1

