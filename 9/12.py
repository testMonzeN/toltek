r = ''
n = 1567
while n > 0:
    r = str(n % 3) + r
    n //= 3

print(r)