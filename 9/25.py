import fnmatch


for x in range(176435003099212, 10 ** 15, 1903):
    if fnmatch.fnmatch(str(x), '176435??31??435') and x % 1903 == 0:
        print(x, x // 1903)