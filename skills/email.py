import smtplib
from email.mime.text import MIMEText
from config import EMAIL, EMAIL_PASSWORD

def send_email(to, subject, body):
    """Sends email via SMTP"""
    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = EMAIL
        msg['To'] = to
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL, EMAIL_PASSWORD)
            server.send_message(msg)
        return "Email sent successfully!"
    except Exception as e:
        return f"Failed to send email: {str(e)}"