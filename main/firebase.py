import os
from django.conf import settings
import firebase_admin
from firebase_admin import credentials, auth, firestore

# Firebase Admin SDK initialization
#json_path = os.path.join(settings.BASE_DIR, 'static', 'restaurant-project-b5ace-firebase-adminsdk-rimn3-4fe154fb20.json')
cred = credentials.Certificate('main/static/restaurant-project-b5ace-firebase-adminsdk-rimn3-4fe154fb20.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def signup_user(email, password, mobile, address):
    try:
        # Create the user in Firebase Auth
        user = auth.create_user(
            email=email,
            password=password
        )

        # Save additional user data in Firestore
        user_data = {
            'name': email.split('@')[0],  # Using email's local part as the name for simplicity
            'mobile': mobile,
            'address': address,
            'password': password
        }
        db.collection('users').document(user.uid).set(user_data)  # Save user data

        return user.uid  # Return the user ID if successful
    except Exception as e:
        print(f"Error creating user: {e}")
        return None  # Return None if there's an error
    


def login_user(email, password):
    try:

        user = auth.get_user_by_email(email)

        user_data = db.collection('users').document(user.uid).get().to_dict()
        if user_data and user_data['password'] == password:
            return {'uid': user.uid, 'data': user_data}  # Return user info on successful login
        else:
            return None

        if user:
            return user  # Return the user's UID upon successful login
        else:
            return None
    except:
        return None