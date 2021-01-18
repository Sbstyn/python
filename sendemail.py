import smtplib

def sendGmail(mailAdress, mailSubject):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("chesscapist@gmail.com", "sodeeP12")
    server.sendmail("chesscapist@gmail.com", mailAdress, mailSubject)

    server.quit()