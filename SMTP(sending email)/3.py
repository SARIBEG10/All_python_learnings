import smtplib as smtp
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import emoji

"""HTML FORMAT EMAIL"""

host = 'smtp.gmail.com'
port = 587
username = 'sfarmanian@gmail.com'
password = 'SariBeg-137216-Farmanian'

connection = smtp.SMTP(host, port)
connection.ehlo()
connection.starttls()
connection.login(username, password)
plain_text = emoji.emojize(':red_heart:')

tmessage = MIMEMultipart()
tmessage['Subject'] = 'html message'
tmessage['From'] = username
tmessage['To'] = username

htm_message = """<html><body><h1>This is My heart give it to you </h1></body></html>"""
msg = MIMEText(htm_message, 'html')
msg2 = MIMEText(plain_text, 'plain')
tmessage.attach(msg)
tmessage.attach(msg2)

connection.sendmail(username, 'Alen_johans96@yahoo.com', tmessage.as_string())
connection.quit()
