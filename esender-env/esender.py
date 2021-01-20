from email.message import EmailMessage
import smtplib

mail_content = "Hello, this is a test email"
smtphost = 'smtp.mail.yahoo.com'
sender_email = 'cykp11@yahoo.com.sg'
sender_pw = 'hcsxjloxlclhpejl'
receiver_email = 'caleby117@gmail.com'

with open('message.txt') as m:
    msgtxt = m.read()

message = EmailMessage()

try: 
    server = smtplib.SMTP_SSL(smtphost, 465)
    server.ehlo()
    server.login(sender_email, sender_pw)
    print(f"Success in connecting to {smtphost}")

except Exception as e: 
    print(e)

server.set_debuglevel(1)
print(server.helo_resp)

message['Subject'] = "Sent from Python"
message['To'] = receiver_email
message['From'] = sender_email
message.set_content(msgtxt)

print(message.keys())

while True:
    confirm = input(f"Sending email from {sender_email} to {receiver_email}, subject {message['Subject']}\n\nPress 'y' to confirm.")
    if confirm == 'y':
        break
try:
    server.send_message(message)

except smtplib.SMTPSenderRefused:
    print("SMTP SenderRefused" + message['sender'])

server.quit()
