from ipaddress import *

net = ip_network('172.16.148.95/255.255.248.0', 0)
for ip in net:
    ip = str(ip).split('.')

    s = 0
    for el in ip:
        s += int(el)

    print(ip, s)