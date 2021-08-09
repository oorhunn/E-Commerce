import smtplib

email = 'anilorhundemiroglu@gmail.com'
password = 'lkllbkwkqolnnvxn'

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(email, password)
    subject = 'anan'
    body = 'baban'
    msg = f'subject: {subject}\n\n {body}'
    smtp.sendmail(email, 'anil_demiroglu@hotmail.com', msg)

