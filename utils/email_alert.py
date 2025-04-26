import smtplib
from email.mime.text import MIMEText

def send_alert(ip, user, pwd, geo):
    msg = MIMEText(f"Intrusion attempt from {ip} ({geo['city']}, {geo['country']})\nUsername: {user}\nPassword: {pwd}")
    msg['Subject'] = '🚨 CyberTrapX Intrusion Detected'
    msg['From'] = 'yourmail@gmail.com' #add ur mail
    msg['To'] = 'yourmail@gmail.com'  #add ur mail

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('youmail@gmail.com', 'password') #add ur mail and password
        smtp.send_message(msg)
