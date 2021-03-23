import os
import smtplib, ssl
from email.mime.text import MIMEText

mail_sender = os.getenv('SENDER_MAIL')
password = os.getenv('MAIL_PASS')

def go_mail(mail, content):
    msg = MIMEText(content, 'html')
    msg['Subject'] = 'News specially choose for you'
    msg['From'] = mail_sender
    msg['To'] = mail
  

    s = smtplib.SMTP_SSL(host='smtp.gmail.com', port = 465)
    s.login(user=mail_sender, password=password)
    s.sendmail(mail_sender, mail, msg.as_string(), content)
    s.quit()