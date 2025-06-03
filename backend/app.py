from flask import Flask, render_template, request, redirect, url_for, flash
from ex import db, bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_cors import CORS



def create_app():
    app = Flask(__name__)
    db.init_app(app)
    bcrypt.init_app(app)
    CORS(app)
    return app  
