# Python Notification Service

This project is a Flask-based API with Celery background task processing for sending email and SMS notifications.

## Features
- Email and SMS notification endpoints
- Asynchronous processing with Celery
- Redis as message broker

## Setup

1. Install Redis
2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run Redis:
   ```
   redis-server
   ```

4. Run the Flask app:
   ```
   python run.py
   ```

5. Start Celery worker:
   ```
   celery -A app.tasks worker --loglevel=info
   ```

## API Endpoints

### POST `/notify/email`
```json
{
  "email": "test@example.com",
  "subject": "Hello",
  "message": "Test email"
}
```

### POST `/notify/sms`
```json
{
  "phone": "+1234567890",
  "message": "Test SMS"
}
```
