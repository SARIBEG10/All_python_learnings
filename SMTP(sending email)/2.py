import smtplib as smtp
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import emoji

"""SENDING EMAIL WITH ATTACHMENT FILE"""


host = 'smtp.gmail.com'
port = 587

username = 'email'
password = 'pass'


email_subject = 'This is attached file '

message = MIMEMultipart()
message['From'] = username
message['To'] = username
message['Subject'] = email_subject

plain_text = 'This is heart  emoji file'
msg = MIMEText(plain_text, 'Plain')
message.attach(msg)

filename = 'heart.txt'
openfile = open(filename, 'rb')
file = openfile.read()

mimeref = MIMEBase('application', 'octet_stream')
mimeref.set_payload(file)
encoders.encode_base64(mimeref)
mimeref.add_header('Content-Disposition', 'openfile;filename='+filename)
message.attach(mimeref)


connection = smtp.SMTP(host, port)
connection.ehlo()
connection.starttls()
connection.login(username, password)
connection.sendmail(username, 'Alen_johans96@yahoo.com', message.as_string())


connection.quit()






