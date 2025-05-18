import smtplib
from email.message import EmailMessage
import os

EMAIL_ADDRESS = os.getenv('EMAIL_USER')     # e.g., your_email@gmail.com
EMAIL_PASSWORD = os.getenv('EMAIL_PASS')    # Gmail app password

def send_email(to_email, subject, message):
    try:
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg.set_content(message)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        print(f"✅ Email sent to {to_email}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
