import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

def send_email(subject, body):
    sender_email = os.getenv("EMAIL_SENDER")
    receiver_email = os.getenv("EMAIL_RECEIVER")
    password = os.getenv("EMAIL_PASSWORD")

    print("Sender:", sender_email)
    print("Receiver:", receiver_email)
    print("Password loaded:", "YES" if password else "NO")

    if not sender_email or not receiver_email or not password:
        raise ValueError("Email credentials not loaded properly from .env")

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.send_message(msg)
            print("✅ Email sent successfully!")
    except Exception as e:
        print("❌ Email sending failed:", e)
