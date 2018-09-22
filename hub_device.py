""" módulo que indicaría según el servicio, a qué concentrador pertenece
el mismo y tendría como resultado su dirección IP. var = ipaddr_hub"""

import requests
from xml.etree import ElementTree

#service_rid = "5407", 5408, 5402, 5403, 5404, 5405
service_rid = (input("Enter a number: "))
# URL Query a QB
ip2 = []
url = 'https://ignetworks.quickbase.com/db/bii35r4k9?a=API_DoQuery&usertoken=b2hjmh_w4i_b2ytd7mdi8jjrpdg8khp8cmwkm6n&apptoken=5dqgv8bnfsyz7dh2wrwdcjcjztf&query={14.EX.' + service_rid + '}&clist=7'
response = requests.get(url)
xml = ElementTree.fromstring(response.content)
for record in xml.findall('record'):
# Logica sobre cada registro
    ip = record.find('ipv4').text
    ip2.append(ip) #//Inseri os IPs na lista#

if len(ip2) == 3:
   print('Tunnel IP is ' + ip2[2])
   returnip1 = ip2[0]  # // primary IP del list#
   returnip2 = ip2[1]  # // second IP del list#
   returnip3 = ip2[2]  # // Tunnel IP 1#
   print('IP Public One ' + returnip1)
   print('Ip Public Two ' + returnip2)
   print('Ip Tunnel One ' + returnip3)

elif len(ip2) == 4:
   print('Tunnel IP is ' + ip2[2] + ' and Tunnel IP is'+ ip2[3])
   returnip1 = ip2[0]  # // primary IP del list#
   returnip2 = ip2[1]  # // second IP del list#
   returnip3 = ip2[2]  # // Tunnel IP 1#
   returnip4 = ip2[3]  # // Tunnel IP 2#
   print('IP Public One '+returnip1)
   print('Ip Public Two '+returnip2)
   print('Ip Tunnel One '+returnip3)
   print('Ip Tunnel Two '+returnip4)

else
   print('Ip para Teste Ip One ' + ip2[0] + ' and IP Two is'+ ip2[1])
   returnip1 = ip2[0]  # // primary IP del list#
   returnip2 = ip2[1]  # // second IP del list#
   print('IP Public One '+returnip1)
   print('Ip Public Two '+returnip2)

ipaddr_tun = ip2[2]; #//Verificar como hacer la prueba
#ipaddr_tun = input('Ingresa direccion IP del servicio: ')

if ipaddr_tun[0:6] in '10.1.7':
    ipaddr_hub = '172.21.4.18'  # MIA1-AR3
elif ipaddr_tun[0:5] in '10.54':
    ipaddr_hub = '172.21.4.66'  # BUE3-AR1
elif ipaddr_tun[0:5] in '10.55':
    ipaddr_hub = '172.21.4.33'  # SAO3-AR1
else:
    ipaddr_hub = '172.21.4.113'  # SCL1-AR1
