
data = []
n_not_mod_2 = []
with open('26.txt') as file:
    _ = file.readline()
    for i in file:
        data.append(int(i))

size = len(data)
k = 0
MAX = 0
for i in range(size - 1):
    for j in range(i + 1, size):
        if data[i]%2==1 and data[j]%2==1 and  (data[i] + data[j]) / 2 in data:
            k += 1
            print(k)
            MAX = max(MAX, (data[i] + data[j]) / 2)

print(k, MAX)