import smtplib
from email.mime.text import MIMEText
import user_cred as cred

def init_mail():
    mail = smtplib.SMTP(cred.mail_creds["SMTP_SERVER"], cred.mail_creds["SMTP_PORT"])
    mail.set_debuglevel(True)
    mail.starttls()
    mail.login(cred.mail_creds["SMTP_USERNAME"], cred.mail_creds["SMTP_PASSWORD"])
    return mail

# mail_content : dict with keys "BODY" AND "EMAIL_SUBJECT"
def send_email(mail_content):
    msg = MIMEText(mail_content["BODY"])
    msg['Subject'] = mail_content["EMAIL_SUBJECT"]
    msg['From'] = cred.mail_creds["EMAIL_FROM"]
    msg['To'] = cred.mail_creds["EMAIL_TO"]

    mail = init_mail()
    mail.sendmail(cred.mail_creds["EMAIL_FROM"], cred.mail_creds["EMAIL_TO"], msg.as_string())

def quit_mail(mail):
    mail.quit()