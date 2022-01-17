from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

msg = MIMEMultipart()

msg['From'] = "me@gmail.com"
password = "1234"

msg['To'] = "Someone"

msg['Subject'] = "This is the Subject"
message = "This is a test"

port = 587

msg.attach(MIMEText(message, "plain"))
server = smtplib.SMTP("smtp.gmail.com", port=port)
server.starttls()
server.login(msg['From'], password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
