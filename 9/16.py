db = {}
for n in range(1, 200030):
    if n == 1:
        db[n] = 1
    elif n > 1:
        db[n] = n * db[n - 1]

print(db[200026] / db[200025])