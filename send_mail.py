import os, smtplib

from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_mail():
    
    load_dotenv(verbose=True)

    mail_user = os.getenv('MAIL_USER')
    mail_pwd = os.getenv('MAIL_PWD')
    mail_dest =os.getenv('MAIL_DEST')

    email_smtp_server = 'smtp.gmail.com'

    destination = ['MAIL_DEST']

    subject = "Teste Bot Python"

    msg = MIMEMultipart()
    msg['From'] = mail_user
    msg['Subject'] = subject
    text = 'Enviando e-mail com python de forma auto'
    msg_text = MIMEText(text, 'html')
    msg.attach(msg_text)


    smtp = smtplib.SMTP(email_smtp_server, 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(mail_user, mail_pwd)
    smtp.sendmail(mail_user, ';'.join(destination), msg.as_string())
    smtp.quit()


send_mail()
