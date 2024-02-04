from flask import Flask, Blueprint
from config import Config
from routes import register_routes
from database import init_app
import os

app = Flask(__name__)
app.config.from_object(Config)

db = init_app(app)

# API Blueprint
api_bp = Blueprint('api', __name__)
app.register_blueprint(api_bp, url_prefix='/api')

register_routes(app)

if __name__ == '__main__':
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    app.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
