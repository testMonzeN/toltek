print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if (not(x and z and not(y)) and not(w and x) and not(not(y or x) == w)) == 1:
                    print(x, y, w, z)

# x y w z
# 0 0 0 1
# 0 1 1 0
# 0 1 1 1