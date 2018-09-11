#from Scratch, By NicoMorra.
#Utilizado nuevo codigo, en vez de utilizar os.system se utiliza el comando subprocess.run (seria la manera mas nueva de implementar la misma tarea)
#Testeando ambas al mismo tiempo se obtiene un mejor resultado de esta nueva manera
#MTR Test, Save File Report, Send Mail with Results.

import subprocess #Para ejecutar comando desde Linux, OSX
import smtplib #Lib Mail
from email.mime.text import MIMEText #Lib Mail
from email.mime.multipart import MIMEMultipart #Lib Mail
from email.mime.base import MIMEBase #Lib Mail
from email import encoders #Lib Mail
#Modulo MTR, agregando import subprocess al inicio
host = str(input('host: ')) #Apertura del dialogo para colocar la direccion hacia la cual hacer el MTR
#Output del subproceso entre () comando ejecutable + Texto de Reporte
output = subprocess.run("mtr --report > Report.txt --report-cycles 10 " + host, shell=True, 
				stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
#Fin Modulo MTR
#Modulo Email integrado al MTR con lectura y envio del Reporte.
email_user = 'ig_bot@ignetworks.com'
email_password = 'password'
email_send = 'noc@ignetworks.com'

subject = 'Report'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'MTR Results!'
msg.attach(MIMEText(body,'plain'))

filename='Report.txt'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit() #Fin del modulo de Email

#Tener en cuenta que para que funcione el modulo de envio de mail desde Python, se debe activar en Google la opcion para que funcione con "Aplicaciones menos seguras"
#ingresando a https://myaccount.google.com/lesssecureapps