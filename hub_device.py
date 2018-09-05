""" módulo que indicaría según el servicio, a qué concentrador pertenece el mismo, y tendría como 
resultado su dirección IP. var = ipaddr_hub"""
from netmiko import ConnectHandler

ipaddr_hub = '0'
ipaddr_tun = str(input('Ingresa direccion IP del servicio: '))
ipaddr_tun = ipaddr_tun[0:5]

if   ipaddr_tun in '10.56. ': 
	 ipaddr_hub =  '172.21.4.113'     #SCL1-AR1
elif ipaddr_tun in '10.54. ':
	 ipaddr_hub = '172.21.4.66'    #BUE3-AR1
elif ipaddr_tun in '10.55. ':
	 ipaddr_hub = '172.21.4.33'    #SAO3-AR1
else:ipaddr_hub = '172.21.4.18'    #MIA1-AR3

print(ipaddr_hub)

#Todo lo que no este en un rango de direccion IP conocido va hacia Miami.
