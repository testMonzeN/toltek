file = open('26.txt', mode='r')

string = file.readline().split()
a = [0 for x in range(6661)]
MAX = 0
while True:
    string = file.readline().split()
    if string:
        rad = int(string[0])
        mesto = int(string[1])

        a[mesto - 1] = rad - 1
        #print(a[mesto - 1])
    else:
        break

print(a)

print(MAX)
