print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if ((w == (y and not(z))) and x) == 1:
                    print(x, y, w, z)