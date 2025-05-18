import json
import os
from datetime import datetime

NOTIFICATION_FILE = os.path.join(os.path.dirname(__file__), 'notifications.json')

def load_notifications():
    if os.path.exists(NOTIFICATION_FILE):
        with open(NOTIFICATION_FILE, 'r') as file:
            return json.load(file)
    return []

def save_notification(message):
    notifications = load_notifications()
    notifications.append({
        'message': message,
        'timestamp': datetime.utcnow().isoformat()
    })
    with open(NOTIFICATION_FILE, 'w') as file:
        json.dump(notifications, file, indent=2)