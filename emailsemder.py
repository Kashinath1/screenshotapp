import smtplib

to = input("Enter the email of recipent:\n")

content = input("enter the content for the mail:\n")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('senderemail@gmail.com', '123')
    server.sendmail('senderemail@gmail.com',to, content)
    server.close()
    
sendEmail(to, content)    
    