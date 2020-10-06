import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class Email:
    def __init__(self, user, password):
        self.__user = user
        self.__password = password

    @property
    def user(self):
        return self.__user

    @property
    def password(self):
        return self.password

    def send_email(self, to, subject, body, attach=None):
        filename = attach.split('\\')[-1]
        msg = MIMEMultipart()
        msg['From'] = self.__user
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(body))

        attachment = open(attach, "rb")

        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        attachment.close()

        encoders.encode_base64(p)
        p.add_header('Content-Disposition',
                     "attachment; filename= %s" % filename)

        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(self.__user, self.__password)

        text = msg.as_string()

        s.sendmail(self.__user, to, text.encode('utf-8'))
        s.quit()

