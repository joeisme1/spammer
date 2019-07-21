print('email spammer')
print('gmail only!!!')
import smtplib
num = 0
uname = input('enter email adress: ')
pword = input('enter password: ')
subject = input('enter subject: ')
message = input('enter message: ')
tget = input('enter target: ')
amount = input('enter amount: ')
def send():
    mail = smtplib.SMTP('smtp.gmail.com:587')
    mail.ehlo()
    mail.starttls()
    mail.ehlo()
    mail.login(uname, pword)
    msg = f'Subject: {subject}n/n/{message}'
    mail.sendmail(uname, tget, msg)
    mail.close()
    num + 1

while 1 == 1:
    send()
    

    if num == amount:
       break
    else:
       print('sent')

print('success')


