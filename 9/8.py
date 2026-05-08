import itertools

k = 1
for x in itertools.product(sorted(['А', 'Л', 'Г', 'О', 'С', 'Ы']), repeat=5):
    string = "".join(x)

    if string[0] not in "АГ" and string.count('Ы') >= 2:
        if k % 2 != 0:
            print(string, k)

    k += 1
