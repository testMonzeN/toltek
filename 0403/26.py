from itertools import permutations

text = []
n_not_mod_2 = []
with open('26.txt') as file:
    _ = file.readline()

    for i in file:
        if int(i) % 2 != 0:
            n_not_mod_2.append(int(i))

        text.append(int(i))

size = len(n_not_mod_2)
k = 0
MAX = 0
for i in range(size - 1):
    for j in range(i + 1, size):
        if (n_not_mod_2[i] + n_not_mod_2[j]) / 2 in text:
            k += 1
            MAX = max(MAX, (n_not_mod_2[i] + n_not_mod_2[j]) / 2)

print(k // 2, MAX)