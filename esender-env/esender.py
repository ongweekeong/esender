from mailsender import MailSender
import database


companies = database.get_companies_from_db('licenses.db')

#print the compnaies info debug
for company in companies:
    if company.is_expired:
        status = f'EXPIRED on {company.get_exp_date_str()}'
    else:
        status = f'Expiry date: {company.get_exp_date_str()}'
    print(f'{company} - {status} {company.tte_days} to expiry')
print()

#creds
smtphost = 'smtp.mail.yahoo.com'
sender_email = 'cykp11@yahoo.com.sg'
sender_pw = 'hcsxjloxlclhpejl'
port = 465

sender = MailSender(sender_email, sender_pw, smtphost, port)
#ehlo the server
sender.connect()

email_txts = {42: {'company': [], 'txt': '6wks.txt'}, 14: {'company': [], 'txt': '2wks.txt'},\
    0: {'company': [], 'txt':'today.txt'}}


##test cases
testcomp1 = {'license': 'PE123456',  'name': 'testcomp1', 'expiry_date': '26/01/2021', \
    'email': 'caleby117@gmail.com'} 
companies.append(database.Company(testcomp1))


testcomp2 = {'license': 'PE123457', 'name': 'testcomp2', 'expiry_date': '9/2/2021', \
    'email': 'caleby117@gmail.com'} 
companies.append(database.Company(testcomp2))
print(companies[-1].tte_days)

testcomp3 = {'license': 'PE123458',  'name': 'testcomp3', 'expiry_date': '9/3/2021', \
    'email': 'caleby117@gmail.com'} 

companies.append(database.Company(testcomp3))


testcomp4 = {'license': 'PE123459',  'name': 'testcomp4', 'expiry_date': '9/3/2021', \
    'email': 'caleby117@gmail.com'} 

companies.append(database.Company(testcomp4))


#add the companies to the list of companies to send emails to
for company in companies:
    if company.tte_days in email_txts.keys():
        email_txts[company.tte_days]['company'].append(company)

for days in email_txts:
    for rec in email_txts[days]['company']:
        sender.add_recepient(rec.email)
        
    sender.set_message_from_txt(email_txts[days]['txt'])
    sender.send_email()
    sender.clear_recepients()
    sender.clear_message()

'''
with open('2wks.txt') as m:
    msgtxt = m.read()
print(f'{repr(msgtxt)}')


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
'''
