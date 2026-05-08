import ipaddress

net = ipaddress.ip_network('91.189.209.206/255.255.248.0', 0)

for ip in net:
    ip = str(ip).split('.')
    print(ip)

print(91 + 189 + 215 + 254)