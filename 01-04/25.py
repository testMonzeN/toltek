'''
TODO
    153) (А. Богданов) Найдите наименьшее натуральное число, которое имеет ровно 1600 делителей.
    В ответе запишите сначала само число и затем его наибольший простой делитель.
    Подсказка: используйте основную теорему арифметики.
'''

def f(x):
    d = []

    i = 2
    while i <= x:
        while x % i == 0:
            d.append(i)
            x //= i
        i += 1
    if d:
        return d


check = int('1' + '000' * 266)
print(f(check), len(f(check))) # 30 36 42 54
while True:
    if len(f(check)) == 1600:
        print(check, max(f(check)))
        break
    check += 1
