"""Email sending functionality."""
import os
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText

load_dotenv()

def send_email(subject: str, content: str, to_address: str = os.getenv("EMAIL_RECIPIENT")):
    """Sends an email with the given subject and content."""
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = os.getenv("SMTP_PORT")
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")
    smtp_sender = os.getenv("SMTP_SENDER")

    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = f"Job Alerts <{smtp_sender}>"
    msg['To'] = to_address

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, [to_address], msg.as_string())
        print(f"Email sent to {to_address}")
