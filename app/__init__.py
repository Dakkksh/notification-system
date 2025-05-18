from flask import Flask
from dotenv import load_dotenv
load_dotenv()

def create_app():
    app = Flask(__name__)
    from .routes import bp as api_bp
    app.register_blueprint(api_bp)
    return app
