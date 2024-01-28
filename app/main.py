from flask import Flask, Blueprint
from config import Config
from routes import register_routes
from database import init_app

app = Flask(__name__)
app.config.from_object(Config)

db = db = init_app(app)

# API Blueprint
api_bp = Blueprint('api', __name__)
app.register_blueprint(api_bp, url_prefix='/api')

register_routes(app)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
