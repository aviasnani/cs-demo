from datetime import datetime, timezone
from extensions import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(50), nullable=False)  # Increased length for names
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email is unique and required
    date_of_birth = db.Column(db.Date, nullable=True)  # Use Date type for DOB
    username = db.Column(db.String(30), unique=True, nullable=False)  # Unique username required
    password = db.Column(db.String(128), nullable=True)  # Nullable if using social login; length to support hashed passwords
    public_key = db.Column(db.Text, nullable=False)  # Use Text if key length varies; not String(300)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))  # Use DateTime with default now()
    provider = db.Column(db.String(20), nullable=False, default='manual')  # e.g., 'google', 'apple', 'manual'