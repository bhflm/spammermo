import smtplib
from keys import *
from email.mime.multipart import MIMEMultipart

def funciona():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(userEmail, userPassword)
    i = 0 # i can make this better this is just a test i swear
    server.sendmail(userEmail, emailTarget, "whatever the fuck")

funciona()
