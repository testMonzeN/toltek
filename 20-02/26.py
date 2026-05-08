'''
 В первой строке входного файла находятся три числа: N – количество занятых мест в зале, М – количество рядов и К – количество, мест в каждом ряду.'''
with open('26.txt') as file:
    N, M, K = map(int, file.readline().split())

    first_rad = [M + 1] * (K + 1)
    for line in file:
        rad, mesto = map(int, line.split())

        if first_rad[mesto] > rad:
            first_rad[mesto] = rad

for rad in range(M - 1, 0, -1):
    for mesto in range(K - 1, 0, -1):
        if first_rad[mesto] > rad and first_rad[mesto + 1] > rad:
            print(rad, mesto + 1)
            exit()