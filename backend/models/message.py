from extenions import db
from datetime import datetime, timezone 

class Message(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  recepient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  encrypted_message = db.Column(db.Text, nullable=False)
  message_type = db.Column(db.String(20), nullable=False)
  timestamp = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))