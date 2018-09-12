# Modulo de diagnostico de servicio degradado con equipo de demarcacion IGN.
from datetime import datetime
from netmiko import ConnectHandler
import user_passw
import hub_device


'''modulo que indicaria segun el servicio, a que concentrador pertenece
el mismo, y tendria como resultado su direcciin IP. var = ipaddr_hub'''

# Conexion al concentrador
# net_connect = ConnectHandler(device_type='cisco_ios_telnet', ip='192.168.5.142', username='ign', password='auto')
start_time = datetime.now()
net_connect = ConnectHandler(device_type='cisco_ios_telnet', ip=hub_device.ipaddr_hub, username=user_passw.user, password=user_passw.passw)

# En el concentrador ejecutar "show ip nhrp ipaddr_tun" y almacenar en la variable ipaddr_nbma
ipaddr_nbma = net_connect.send_command('show ip nhrp ' + hub_device.ipaddr_tun + ' | i NBMA')
ipaddr_nbma = ipaddr_nbma[16:].replace(' ', '')

# Perdidas fuera del tunel (por ende tambien dentro)
# ping fuera del tunel
ping_out = net_connect.send_command(
    'ping ' + ipaddr_nbma + ' repeat 100 timeout 1')

# ping dentro del tunel
ping_in = net_connect.send_command(
    'ping ' + hub_device.ipaddr_tun + ' repeat 100 timeout 1')
net_connect.disconnect()
print('#'*7)
print(ping_out)
print('#'*7)
print(ping_in)
print('#'*7)

# Generar variable de modelo del equipo
net_connect = ConnectHandler(
    device_type='cisco_ios_telnet', ip=hub_device.ipaddr_hub,
    username=user_passw.user, password=user_passw.passw)

dev_vers = net_connect.send_command('show version | include Cisco')
dev_vers = dev_vers[19:25].replace(' ', '')
dev_vers = dev_vers.replace(',', '')

# Verificar contadores y negociacion de la interfaz conectada al proveedor
if dev_vers in 'C8':
    inet_counters_vendor = net_connect.send_command(
        'show interfaces fastethernet4 | i duplex|CRC|collision|Last clearing|Description')
    inet_counters_cust = net_connect.send_command(
        'show interfaces fastethernet1 | i duplex|CRC|collision|Last clearing|Description')
    net_connect.disconnect()
else:
    inet_counters_vendor = net_connect.send_command(
        'show interfaces fastethernet0/0 | i duplex|CRC|collision|Last clearing|Description')
    inet_counters_cust = net_connect.send_command(
        'show interfaces fastethernet1/1 | i duplex|CRC|collision|Last clearing|Description')
    net_connect.disconnect()


print('*'*5, 'ISP Interface', '*'*5)
print(inet_counters_vendor)
print('*'*5, 'Customer Interface', '*'*5)
print(inet_counters_cust)

# Perdidas dentro del tunel
# show processes cpu | i utilization
# CPU utilization for five seconds: 2%/0%; one minute: 7%; five minutes: 4%

end_time = datetime.now()
total_time = end_time - start_time
print('_'*5)
print('Duracion:', total_time)
print('_'*5)
