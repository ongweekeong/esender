from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

mail_content = "Hello, this is a test email"
smtphost = 'smtp.mail.yahoo.com'
sender_email = 'cykp11@yahoo.com.sg'
sender_pw = 'hcsxjloxlclhpejl'


try: 
    server = smtplib.SMTP_SSL(smtphost, 465)
    server.ehlo()
    server.login(sender_email, sender_pw)
    print(f"Success in connecting to {smtphost}")

except Exception as e: 
    print(e)
