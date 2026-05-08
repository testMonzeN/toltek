import ipaddress

net = ipaddress.ip_network('6.4.20.26/255.255.128.0', 0)
for ip in net:
    ip2 = str(ip).split('.')
    s = 0
    for el in ip2:
        s += int(el)

    print(s)