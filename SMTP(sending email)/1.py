import smtplib as smtp

"""PLAIN TEXT EMAIL"""

host = 'smtp.gmail.com'
port = 587
username = 'email'
password = 'pass'

connection = smtp.SMTP(host, port)
connection.ehlo()
connection.starttls()
connection.login(username, password)
message = "hello dear friend".title()
connection.sendmail(username, username, message)
connection.quit()










