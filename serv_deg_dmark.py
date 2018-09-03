#Módulo de diagnóstico de servicio degradado con equipo de demarcación IGN.

# Importar la función ConnectHanler de la librería netmiko
from netmiko import ConnectHandler

""" módulo que indicaría según el servicio, a qué concentrador pertenece el mismo, y tendría como 
resultado su dirección IP. var = ipaddr_hub"""
import which_hub 

#Conexión al concentrador
#net_connect = ConnectHandler(device_type='cisco_ios_telnet', ip='192.168.5.142', username='ign', password='auto')
net_connect = ConnectHandler(device_type='cisco_ios_telnet', ip=ipaddr_hub, username=user_passw.user, password=user_passw.passw) 

#En el concentrador ejecutar "show ip nhrp ipaddr_tun" y almacenar en la variable ipaddr_nbma
ipaddr_nbma = net_connect.send_command('show ip nhrp '+ ipaddr_tun)
ipaddr_nbma = ipadrr_nbma[17:30].replace[' ','']
#MIA1-AR3#show ip nhrp 10.1.78.5 | include NBMA address
#  NBMA address: 190.80.136.7
#    (Claimed NBMA address: 10.0.0.2)

#ping ip_addr_tun timeout 1 repeat 1000 --> Ping por dentro del tunnel
#ping nbma_addr timeout 1 repeat 1000 size 1500 source net_lpb_addr --> Ping por afuera del tunnel

###Resultados###
###Sin pérdidas
#Verificar contadores y negociación de las interfaz conectada al cliente

##show interfaces interfaces_to_cust | i duplex|CRC|collision|Last clearing
 #Full-duplex, 100Mb/s, 100BaseTX/FX
 #Last clearing of "show interface" counters 00:00:06
 #   0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
 #   0 output errors, 0 collisions, 0 interface resets
 #   0 babbles, 0 late collision, 0 deferred

###Pérdidas fuera del túnel (por ende también dentro)


net_connect = ConnectHandler(device_type='cisco_ios_telnet', ip=ipaddr, username=user, password=passw) 

ping = net_connect.send_command("ping 192.168.5.2")
#Verificar contadores y negociación de la interfaz conectada al proveedor
##show interfaces interfaces_to_cust | i duplex|CRC|collision|Last clearing
 #Full-duplex, 100Mb/s, 100BaseTX/FX
 #Last clearing of "show interface" counters 00:00:06
 #   0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
 #   0 output errors, 0 collisions, 0 interface resets
 #   0 babbles, 0 late collision, 0 deferred

###Pérdidas dentro del túnel
#show processes cpu | i utilization
#CPU utilization for five seconds: 2%/0%; one minute: 7%; five minutes: 4%

#$$$No me gusta$$$#
#show running-configuration interface tunnel_x | i mtu
#ip mtu 1400

