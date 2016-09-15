# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 05:21:57 2016

@author: pratikgujral
"""

def send_email(sender_email, password, recipient_email, subject, body):
    import smtplib
    print sender_email
    print password
    print recipient_email
    print subject
    print body
    #message = "\r\n".join("FROM: %s", "TO: %s", "SUBJECT: %s","", "%s" % (sender_email, recipient_email, subject,body))
    message = "FROM: "+sender_email+"\r\nTO: "+recipient_email+"\r\nSUBJECT: "+subject+"\r\n"+body
    print message
    try:
        server = smtplib.SMTP(host = 'smtp.gmail.com', port=587)
        server.ehlo()
        server.starttls()
        server.login(user = sender_email, password = password)
        server.sendmail(sender_email, recipient_email, message)
        server.close()
        print "Successfully send the email"
    except Exception, e:
        print "Exception occurred:", e
    
email_to = r"pratikgujral@outlook.com"
email_from = r"pratikgujral@gmail.com"

####   TO-DO
password= "" # PASSWORD HERE
subject = "Hi from Python"
body= "This is a test email from the Python Script"

send_email(email_from, password, email_to, subject, body)
