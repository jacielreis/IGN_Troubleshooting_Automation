from netmiko import ConnectHandler

cisco_7200 = {
'device_type': 'cisco_ios',
'ip': '192.168.122.108',
'username': 'python',
'password': 'python',
 }

net_connect = ConnectHandler(device_type='cisco_ios', ip=‘192.168.122.108’, username=‘python’, password=‘python’)

net_connect.find_prompt()
