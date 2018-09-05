#Módulo de diagnóstico de servicio degradado con equipo de demarcación IGN.

# Importar la función ConnectHanler de la librería netmiko
from netmiko import ConnectHandler
from datetime import datetime

""" módulo que indicaría según el servicio, a qué concentrador pertenece el mismo, y tendría como 
resultado su dirección IP. var = ipaddr_hub"""
import hub_device 

#Conexión al concentrador
#net_connect = ConnectHandler(device_type='cisco_ios_telnet', ip='192.168.5.142', username='ign', password='auto')
net_connect = ConnectHandler(device_type='cisco_ios_telnet', ip=hub_device.ipaddr_hub, username=user_passw.user, password=user_passw.passw) 

#En el concentrador ejecutar "show ip nhrp ipaddr_tun" y almacenar en la variable ipaddr_nbma
ipaddr_nbma = net_connect.send_command('show ip nhrp '+ ipaddr_tun)
ipaddr_nbma = ipadrr_nbma[17:30].replace(' ','')

###Pérdidas fuera del túnel (por ende también dentro)
#Analizar el ping
ping = net_connect.send_command('ping ' + ipaddr_nbma + ' repeat 100 timeout 1')
print(ping)
net_connect.disconnect() 

#Generar variable de modelo del equipo
net_connect = ConnectHandler(device_type='cisco_ios_telnet', ip=ipaddr_tun, username=user_passw.user, password=user_passw.passw) 
dev_vers = net_connect.send_command('show version | include Cisco')
dev_vers = dev_vers[18:25].replace(' ','')
dev_vers = dev_vers.replace(',','')
net_connect.disconnect() 

#Verificar contadores y negociación de la interfaz conectada al proveedor
if dev_vers in 'C8':
	net_connect = ConnectHandler(device_type='cisco_ios_telnet', ip='192.168.5.142', username='ign', password='auto')
	inet_counters = net_connect.send_command('show interfaces fastethernet4 | i duplex|CRC|collision|Last clearing|Description')
	net_connect.disconnect()
else:
	net_connect = ConnectHandler(device_type='cisco_ios_telnet', ip='192.168.5.142', username='ign', password='auto')
	inet_counters = net_connect.send_command('show interfaces fastethernet0/0 | i duplex|CRC|collision|Last clearing|Description')
	net_connect.disconnect()

print(inet_counters)

#Verificar contadores y negociación de la interfaz conectada al proveedor
if dev_vers in 'C8':
	net_connect = ConnectHandler(device_type='cisco_ios_telnet', ip='192.168.5.142', username='ign', password='auto')
	inet_counters = net_connect.send_command('show interfaces fastethernet1 | i duplex|CRC|collision|Last clearing|Description')
	net_connect.disconnect()
else:
	net_connect = ConnectHandler(device_type='cisco_ios_telnet', ip='192.168.5.142', username='ign', password='auto')
	inet_counters = net_connect.send_command('show interfaces fastethernet0/1 | i duplex|CRC|collision|Last clearing|Description')
	net_connect.disconnect()

print(inet_counters)

#ping ip_addr_tun timeout 1 repeat 100 --> Ping por dentro del tunnel

###Pérdidas dentro del túnel
#show processes cpu | i utilization
#CPU utilization for five seconds: 2%/0%; one minute: 7%; five minutes: 4%

end_time = datetime.now()
total_time = end_time - start_time
print(total_time)
#$$$No me gusta$$$#
#show running-configuration interface tunnel_x | i mtu
#ip mtu 1400
