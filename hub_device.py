""" módulo que indicaría según el servicio, a qué concentrador pertenece
el mismo y tendría como resultado su dirección IP. var = ipaddr_hub"""
import requests
from xml.etree import ElementTree
########## IMPORTAR MODO DE ZENDESK################
#service_rid = "5407", 5408, 5402, 5403, 5404, 5405
service_rid = (input("Enter a number: "))
# URL Query a QB
ipaddr2 = []
url = 'https://ignetworks.quickbase.com/db/bii35r4k9?a=API_DoQuery&usertoken=b2hjmh_w4i_b2ytd7mdi8jjrpdg8khp8cmwkm6n&apptoken=5dqgv8bnfsyz7dh2wrwdcjcjztf&query={14.EX.' + service_rid + '}&clist=7'
response = requests.get(url)
xml = ElementTree.fromstring(response.content)
for record in xml.findall('record'):
# Logica sobre cada registro
    ipaddr = record.find('ipv4').text
    ipaddr2.append(ipaddr) #//Inseri os IPs na lista#

if len(ipaddr2) == 3:
   ipaddr_tun = ipaddr2[-1];  # //Verificar como hacer la prueba
   if ipaddr_tun[0:6] in '10.1.7':
       ipaddr_hub = '172.21.4.18'  # MIA1-AR3
   elif ipaddr_tun[0:5] in '10.54':
       ipaddr_hub = '172.21.4.66'  # BUE3-AR1
   elif ipaddr_tun[0:5] in '10.55':
       ipaddr_hub = '172.21.4.33'  # SAO3-AR1
   else:
       ipaddr_hub = '172.21.4.113'  # SCL1-AR1

elif len(ipaddr2) == 4:
   ipaddr_tun = ipaddr2[-1];  # //Verificar como hacer la prueba
   if ipaddr_tun[0:6] in '10.1.7':
       ipaddr_hub = '172.21.4.18'  # MIA1-AR3
   elif ipaddr_tun[0:5] in '10.54':
       ipaddr_hub = '172.21.4.66'  # BUE3-AR1
   elif ipaddr_tun[0:5] in '10.55':
       ipaddr_hub = '172.21.4.33'  # SAO3-AR1
   else:
       ipaddr_hub = '172.21.4.113'  # SCL1-AR1
else:
   ipaddr_tun = ipaddr2[-1];  # //Verificar como hacer la prueba
   if ipaddr_tun[0:6] in '10.1.7':
       ipaddr_hub = '172.21.4.18'  # MIA1-AR3
   elif ipaddr_tun[0:5] in '10.54':
       ipaddr_hub = '172.21.4.66'  # BUE3-AR1
   elif ipaddr_tun[0:5] in '10.55':
       ipaddr_hub = '172.21.4.33'  # SAO3-AR1
   else:
       ipaddr_hub = '172.21.4.113'  # SCL1-AR1

#ipaddr_tun = ipaddr2[2]; #//Verificar como hacer la prueba
#ipaddr_tu
