import smtplib
import os
import random
from keys import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders


def getRandomPic():
    files = []
    for filename in os.listdir(directory):
        files.append(filename)
    return str(directory + random.choice(files))

def gedear():

    msg = MIMEMultipart()
    msg['From'] = userEmail
    msg['To'] = ", ".join(targets) #multiple recipients: targets should be an array of emails for it to work.
    #msg['To'] = targets >>> this should be a single email in case gedear is chilly
    msg['Subject'] = customSubject
    body = customBody
    msg.attach(MIMEText(body,'plain'))

    filename = getRandomPic()
    attachment = open(filename,'rb')

    # all the encoding bs for uploading just a simple jpg to an email with MIME
    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    #format this mf for email
    msg.attach(part)
    text = msg.as_string()

    server = smtplib.SMTP(googleHost, googlePort)
    server.starttls()
    server.login(userEmail, userPassword)
    server.sendmail(userEmail, targets, text)
    server.quit()

gedear()
