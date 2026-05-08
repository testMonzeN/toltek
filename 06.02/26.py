with open('26.txt') as file:
    size = file.readline()
    balls = file.readline().split() # ['100', '90']

    text = file.readlines()

l = [] #[id, summ(test1, test2, ...)]
for i in text:
    s_pol = 0 
    s_shtraf = 0 
    k_pass = 0 
    
    
    k = 0 # счетчик
    string = i.split()
    ID = int(string[0])


    for test in string[1::]:
        if test == '1':
            s_pol = s_pol + int(balls[k])
            k += 1
        elif test == '-1':
            s_shtraf = s_shtraf + int(balls[k])
            k += 1
        elif test == '0':
            k_pass += 1
            k += 1

    l.append([ID, s_pol, s_shtraf, k_pass])

print(l)
for i in range(len(l) - 1):
    for j in range(len(l)):
        if l or 
                
    
