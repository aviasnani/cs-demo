from flask import Flask, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS
from flask_session import Session
from flask_wtf.csrf import CSRFProtect
from extensions import db
from models.message import Message
from routes.user_routes import user_bp
from routes.auth_routes import auth_bp
from services.messaging.socket_handler import SocketHandler

app = Flask(__name__)
CORS(app, supports_credentials=True)
socketio = SocketIO(app, cors_allowed_origins="*")

# Security configurations
app.config['SECRET_KEY'] = 'pus-avi-gar-adi-secret-key'  # Change this in plive
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Strict'

# Initialize security extensions
Session(app)
csrf = CSRFProtect(app)

# Register blueprints
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/api/auth')

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Initialize socket handler
socket_handler = SocketHandler(socketio)

@app.route('/')
def index():
    return jsonify({"status": "ok", "message": "Server is running"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    socketio.run(app, debug=True)
