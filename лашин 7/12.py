r = ''
n = 34066

while n > 0:
    r = str(n % 3) + r

    n //= 3

print(r)