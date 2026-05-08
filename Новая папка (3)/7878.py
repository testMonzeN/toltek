with open('26.txt') as file:
    size = int(file.readline())

    req = file.readlines()

avto=[]
for data in req:
    data = data.split()
    avto.append([int(data[0]),int(data[1]),int(data[2])])
    
for i in range(0,size-1):
    for j in range(i+1,size):
        if avto[i][0]>avto[j][0] or (avto[i][0]==avto[j][0]  and avto[i][2]>avto[j][2] ):
            temp = avto[i]
            avto[i]=avto[j]
            avto[j]=temp


            
i=0
while i<len(avto)-1:
    if avto[i][0]==avto[i+1][0] and avto[i][2]==avto[i+1][2]:
        avto[i][1]+=avto[i+1][1]
        avto.pop(i+1)
    else:
        i=i+1
size = len(avto)
for i in range(0,size-1):
    for j in range(i+1,size):
        if avto[i][1]<avto[j][1]:
            temp = avto[i]
            avto[i]=avto[j]
            avto[j]=temp

print(avto)
