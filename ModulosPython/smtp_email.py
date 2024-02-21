import os
import string
import smtplib
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


html_path = os.path.join(os.path.abspath('.'), "smtp_email.html")

load_dotenv()

user = os.getenv("BD_USER")
destiny = user
password = os.getenv("BD_PASSWORD")

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = user
smtp_password = password

with open(html_path, 'r') as file_:
    text = file_.read()
    template = string.Template(text)
    email_text = template.substitute(nome="nine")
    
mime_multipart = MIMEMultipart()
mime_multipart['from'] = user
mime_multipart['to'] = destiny
mime_multipart['subject'] = 'Assunto do email'

mime_text = MIMEText(email_text, 'html', 'utf-8')
mime_multipart.attach(mime_text)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.send_message(mime_multipart)