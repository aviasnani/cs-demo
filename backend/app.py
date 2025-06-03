from flask import Flask, render_template, request, redirect, url_for, flash
from extensions import db, bcrypt
from models.user import User
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_cors import CORS



def create_app():
    app = Flask(__name__)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "user_login"


    @login_manager.user_loader
    def load_user(user_id): 
        return User.query.filter_by(id=int(user_id)).first() 
