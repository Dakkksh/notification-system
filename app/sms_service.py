from twilio.rest import Client
import os

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE')

def send_sms(to_phone, message):
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        msg = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=to_phone
        )
        print(f"✅ SMS sent: {msg.sid}")
    except Exception as e:
        print(f"❌ Failed to send SMS: {e}")
