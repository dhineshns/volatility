import email_utils as ema

def t_send_email():
    try:
        mail = ema.init_mail()
        ema.send_email(mail, {"BODY":"test body", "EMAIL_SUBJECT" : "test email subject"})
        ema.quit_mail(mail)
    except Exception as e:
        print ("Error : The email test failed" + e)

if __name__ == "__main__":
    t_send_email()