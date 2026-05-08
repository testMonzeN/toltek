'''
TODO	(№ 7962) (А. Кабанов)
        Обозначим через D(N) наименьший простой делитель целого числа, оканчивающийся на 777 и не равный самому числу.
        Если таких делителей у числа нет, то считаем значение D(N) равным нулю.
        Найдите наименьшие 4 числа, большие 55 000 000, для которых D(N) > 0.

TODO    В ответе запишите найденные числа в порядке возрастания значений D(N), справа от каждого запишите соответствующее значение D(N).

'''
def d(n: int) -> int:
    MAX = 999999999999999999999999
    for div in range(777, n, 1000):
        if n % div == 0:
            if str(div)[-1] == '7' and str(div)[-2] == '7' and str(div)[-3] == '7':
                ok = True
                for i2 in range(2, int(div ** 0.5) + 1):
                    if div % i2 == 0:
                        ok = False
                        break
                if ok:
                    MAX = min(MAX, div)
    if MAX != 999999999999999999999999:
        return MAX
    else:
        return 0



check = 55_000_000
c = 0
res = []
while c < 4:
    if d(check) > 0:
        res.append([check, d(check)])
        c += 1

    check += 1

res = sorted(res, key=lambda y:y[1])
print(res)