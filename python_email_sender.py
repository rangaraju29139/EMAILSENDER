import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl 
import smtplib



load_dotenv()

sender_email = os.getenv('sender_email')
password = os.getenv('password')

receiver_email = "jojib68551@sportrid.com"



subject = "dont forget to subscribe "

body = """
when you watch a video please subscribe
"""

em = EmailMessage()


em['From'] = sender_email
em['To'] = sender_email
em['Subject'] = subject
em.set_content(body)



context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context = context) as smtp:
    smtp.login(sender_email,password)
    smtp.sendmail(sender_email,receiver_email,em.as_string())
    print("email sent")
    




