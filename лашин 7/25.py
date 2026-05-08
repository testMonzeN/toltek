from fnmatch import fnmatch

for i in range(0, 10 ** 10, 13245):
    if fnmatch(str(i), '43?9*12?'):
        print(i,i // 13245)