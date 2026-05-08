'''
TODO (№ 5226) Пусть N(k) = 19 500 000 + k, где k – натуральное число.
            Найдите пять наименьших значений k, при которых N(k) нельзя представить в виде произведения трёх натуральных чисел, больших 1.
            В ответе запишите найденные значения k в порядке убывания, справа от каждого значения запишите наибольший делитель N(k), не равный самому числу.
'''
def a(n: int) -> bool:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def f(n: int) -> list:
    d = []
    for div in range(2, int(n ** 0.5) + 1):
        if n % div == 0:
            if a(n // div) == True:
                d.append(n // div)
            return [a(n // div), d]

k = 1
c = 0
while c < 5:
    check = 19_500_000 + k
    if f(check)[0]:
        print(k, max(f(check)[1]))
        c += 1

    k += 1
