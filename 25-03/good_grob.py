eda = [0] * 2027
ne_eda = [0] * 2027


with open('26.txt', mode='r') as file:
    size = int(file.readline())

    for line in file:
        a1, a2 = line.split()
        if a2 == 'meal':
            eda[int(a1)] += 1

        else:
            ne_eda[int(a1)] += 1

super = 0
ne_super = 0
print(eda[31], eda[2026 - 31], eda[1013] ,eda)
print(ne_eda[31], ne_eda[2026 - 31], ne_eda[1013], ne_eda)
for i in range(1, 1013):
    if eda[i] != 0:

        min1 = min(eda[i], ne_eda[2026 - i])
        min2 = min(ne_eda[i], eda[2026 - i])

        min3 = min(eda[i] - min1, eda[2026 - i] - min2)
        min4 = min(ne_eda[i] - min2, ne_eda[2026 - i] - min1)

        if i == 31:
            print(min1, min2)
            print(min3, min4)

        super = super + min1 + min2
        ne_super = ne_super + min3 + min4

if eda[1013] != 0 or ne_eda[1013] != 0:
    min1 = min(eda[1013], ne_eda[1013])

    max1 = max(eda[1013], ne_eda[1013]) - min1
    super = super + min1
    ne_super = ne_super + (max1 // 2)
    print(min1, max1 // 2)
print(ne_super + super, ne_super * 2025 + super * 2026)

