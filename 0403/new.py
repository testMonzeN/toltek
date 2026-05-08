def f(n):
    for d in range(2,int(n**0.5)+1):
        if n%d ==0:
            return False
    return True

def check(n):
    for d in range(2,int(n**0.5)+1):
        if n%d ==0:
            return f(n//d)
    return True

for k in range(1,1000):
    if check(19500000+k):
        print(k)

