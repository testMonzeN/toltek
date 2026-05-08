file = open('24.txt')



MINN = 99999999999999999999999999999999999999999999999999
len_ = 0
l = []
k = 0
summ = 0

element = file.read(1)
while True:
    element = file.read(1)
    if not element:
        break

    else:
        if element not in '0123456789':
            len_ += 1

        elif element in '0123456789':
            now = file.read(1)
            if k < 10000:
                if len_!=0:    
                    l.append(len_ + 2)
                    k += 1
                summ += len_
                len_ = 0
            else:
                MINN = min(MINN, summ)
                if len_ == 0:
                    print(222222222)
                summ = summ - l[0] + len_
                l.pop(0)
                l.append(len_ + 2)
                len_ = 0
                

print(MINN) 
file.close()
