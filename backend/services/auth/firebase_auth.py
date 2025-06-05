import firebase_admin
from firebase_admin import credentials, auth
from models.user import User
from extensions import db

class FirebaseAuthService:
    def __init__(self):
        # Initialize Firebase
        cred = credentials.Certificate('add hereXXXXXX /serviceAccountKey.json')
        firebase_admin.initialize_app(cred)

    def verify_firebase_token(self, id_token):
        """Verify Firebase ID token and return user info"""
        try:
            decoded_token = auth.verify_id_token(id_token)
            return decoded_token
        except Exception as e:
            raise ValueError(f"Invalid Firebase token: {str(e)}")

    def get_or_create_user(self, firebase_user):
        """Get existing user or create new one"""
        user = User.query.filter_by(firebase_uid=firebase_user['uid']).first()
        
        if not user:
            # Create new user
            user = User(
                firebase_uid=firebase_user['uid'],
                email=firebase_user.get('email'),
                username=firebase_user.get('name'),
                profile_picture=firebase_user.get('picture')
            )
            db.session.add(user)
            db.session.commit()
        
        return user 