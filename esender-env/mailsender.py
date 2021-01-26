from email.message import EmailMessage
import smtplib

class MailSender():
    '''
    MailSender object:
        @attributes:
            sender_email                        Sender's email address
            smtphost                            Sender's SMTP host
            sender_pw                           Sender's password
            mail_content                        Content of the email
            connected                           Bool: True if the server has been ehlo'ed
            message                             EmailMessage Object
            recipients                          List of recipients of the email
        @methods:
            connect():                          Tries a connection to the SMTP server via SSL and ehlo's it
            add_recipient:                      Adds a recipient to the recipient list

            set_message_from_txt(txtfile):      Reads <txtfile> as message content.
                                                "Subject: <subject>" header on line 1 needed, or set subject manually
            send_email():                       Sends the email to recipients
            clear_recipients():                 Clears the recipients list
    '''

    def __init__(self, sender, sender_pw, smtphost, port):
        self.sender_email = sender
        self.smtphost = smtphost
        self.sender_pw = sender_pw
        self.mail_content = None
        self.connected = False

        self.message = EmailMessage()
        self.message['From'] = sender

        #email addresses of recipients
        self.recipients = []

        try:
            self.server = smtplib.SMTP_SSL(smtphost, port)
        except Exception as e:
            self.server = None
            print("Could not connect to server")
            print(e)

    def connect(self):
        try:
            if not self.server:
                raise ValueError("ERROR: Could not connect to server via SSL")
            self.server.ehlo()
            self.server.login(self.sender_email, self.sender_pw)
            print(f"Success in connecting to {self.smtphost}")

        except Exception as e:
            raise e
        else:
            self.connected = True

    def add_recepient(self, recipient):
        self.recipients.append(recipient)
        del self.message['To']
        if len(self.recipients) == 1:
            self.message['To'] = self.recipients[0]
        else:
            self.message['To'] = self.recipients

    def set_message_from_txt(self, txt):
        with open(txt, encoding='utf-8') as f:
            lines = f.readlines()
        subj_line = lines[0]
        self.mail_content = ''.join(lines[1:])

        if "SUBJECT:" not in subj_line.upper():
            print("WARNING: NO SUBJECT LINE IN TXT")
            #if no subject line, take the entire txt as the message body
            self.mail_content = ''.join(lines)
        else:
            self.message['Subject'] = subj_line[len('subject:'):].lstrip()

        print(repr(self.mail_content))
        self.message.set_content(self.mail_content)
        self.message.preamble = ''

    def clear_message(self):
        del self.message['Subject']
        self.mail_content = ''


    def send_email(self):
        if not self.message['To']:
            print("Could not send email as there are no recipients")
            return

        if not self.message.get_content():
            print("Could not send email as there is no email body")

        if not self.message['Subject']:
            while True:
                cont = input("Warning: Message has no subject. Send anyway?(y/n)")
                if cont == 'y':
                    break
                elif cont == 'n':
                    print("Email not sent")
                    return
                else:
                    print("y/n only")

        if not self.connected:
            self.connect()
        print(self.message['To'])

        self.server.send_message(self.message)

    def clear_recepients(self):
        del self.message['To']
        self.recipients = []


