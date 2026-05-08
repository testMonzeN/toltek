def is_prime(x):
    if x == 2:
        return True

    if x % 2 == 0:
        return False

    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False

    return True

def f(x):
    for i in range(2, int(check ** 0.5) + 1):
        if x % i == 0:
            pather = x // i

            if is_prime(i) == True and is_prime(pather) == True:
                if str(i).count('3') >= 1 and str(pather).count('3') >= 1:
                    return [i, pather]
    return []

check = 6_999_124
c = 0
while c < 6:
    if f(check):
        print(check, max(f(check)))
        c += 1

    check += 1

# 6999127 132059
# 6999161 538397
# 6999177 2333059
# 6999187 538399
# 6999197 5003
# 6999207 2333069