#Run gpedit.msc
#Computer Configuration -> Windows Settings -> Scripts -> Shutdown -> Properties -> Add

# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import datetime
 
# create message object instance
msg = MIMEMultipart()
 
Date = str(datetime.datetime.now().strftime('%d/%m/%Y'))
Time = str(datetime.datetime.now().strftime('%H:%M'))

message = F'Computer Status: ON \n {Time} \n {Date}'
#message = F'Computer Status: OFF \n {Time} \n {Date}'
 
# setup the parameters of the message
password = "william05"
msg['From'] = "william.delmanto@wellcare.com.br"
msg['To'] = "wrdelmanto@gmail.com"
msg['Subject'] = "ON/OFF PC Status"
 
# add in the message body
msg.attach(MIMEText(message, 'plain'))
 
#create server
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
print('--------------------------------')
print (F"Successfully sent email to: \n{msg['To']}")
print('--------------------------------')