from ipaddress import *

net = ip_network('172.16.160.0/255.255.240.0', 0)
for ip in net:
    ip = str(ip).split('.')

    ip2 = 0
    for el in ip:
        ip2 = ip2 + bin(int(el))[2:].count('1')

    if ip2 % 5 == 0:
        s = 0
        for el in ip:
            s += int(el)

        print(1, ip, s)

    print(ip)