from flask import Flask, render_template, request, jsonify
from app.email_service import send_email  # if used
from app.sms_service import send_sms      # if used
from app.notification_model import save_notification, load_notifications

app = Flask(__name__)

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    message = data.get('message', 'No message provided')
    # Here you would call the original messaging logic (e.g., send_email or send_sms)
    save_notification(f"New message received: {message}")
    return jsonify({'status': 'success', 'message': 'Message received and notification stored'})

@app.route('/notifications')
def notifications():
    return render_template('notifications.html', notifications=load_notifications())