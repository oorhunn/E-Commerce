import smtplib

email = 'anilorhundemiroglu@gmail.com'
password = 'lkllbkwkqolnnvxn'
# tubitak 1505 projesi odtu bilgisayar spark ortak projesi teidep
sendmail = 'anil_demiroglu@hotmail.com'

def mailer(sendmail, subject, body):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(email, password)
        msg = f'subject: {subject}\n\n {body}'
        smtp.sendmail(email, sendmail, msg)


