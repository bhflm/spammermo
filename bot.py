import smtplib
import os
from keys import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

def gedear():

    msg = MIMEMultipart()
    msg['From'] = userEmail
    msg['To'] = ", ".join(targets) #multiple recipients: targets should be an array of emails for it to work.
    #msg['To'] = targets >>> this should be a single email in case gedear is chilly
    msg['Subject'] = 'D A N K  D O G G O'
    body = 'G O O D   B O I I I <3' # WHOS A GOOD BOIIII ???? <3
    msg.attach(MIMEText(body,'plain'))

    filename = pic
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

# #evil purposes:
# # def main():
# #     for x in range (5):
# #         print("going for the " + str(x) + "nth SEXY TIME")
# #         gedear()
# main()
