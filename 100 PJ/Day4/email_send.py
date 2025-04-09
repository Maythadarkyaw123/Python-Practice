import smtplib

def sendMail():
    server = smtplib.SMTP('smtp.gmail.com',587) #transport layer security
    server.starttls()
    server.login('ur@gmail.com','psw123')
    server.sendmail('ur@gmail.com', 'to@gmail.com', 'Text msg')
    server.close()
    
sendMail()
    