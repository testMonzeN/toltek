for i in range(6651220, 6653369+1):
    k = 0
    d1 = 0
    d2 = 0
    for d in range(2, i // 2 + 1):
        if i % d == 0:
            if k == 0:
                d1 = d
                k += 1
                if i == d*d:
                    d2 = d
                    k = k + 1
            elif k == 1:
                d2 = d
                k += 1
            else:
                k = -1
                break
    if k == 2:
        if str(d1).count('2') == 1 and str(d2).count('2') == 1: 
            print(i, d1, d2)
    
