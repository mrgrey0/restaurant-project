import os
from django.conf import settings
import firebase_admin
from firebase_admin import credentials, auth, firestore

cred = credentials.Certificate('main/static/restaurant-project-b5ace-firebase-adminsdk-rimn3-bfaa341140.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def signup_user(name, email, password, mobile, address,hotel_login):
    try:
        # Create the user in Firebase Auth
        user = auth.create_user(
            email=email,
            password=password
        )

        # Save additional user data in Firestore
        user_data = {
            'name': name,
            'mobile': mobile,
            'address': address,
            'password': password,
            'hotel_login': hotel_login,
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
    except Exception as e:
        print(e)
        return None
    

def store_order(user_id, food_name, food_price, food_description, delivery_address, user_name, user_num):
    try:
        # Create a reference to the orders collection
        orders_ref = db.collection('orders')

        # Create an order document
        order_data = {
            'user_id': user_id,
            'user_name' : user_name,
            'user_num' : user_num,
            'food_name': food_name,
            'food_price': food_price,
            'food_description': food_description,
            'delivery_address': delivery_address,
            'status': 'Pending',
        }

        # Add the order to Firestore
        orders_ref.add(order_data)

        return True
    except Exception as e:
        print(f"Error storing order: {e}")
        return False
    

def get_pending_orders():
    try:
        orders_ref = db.collection('orders').where('status', '==', 'Pending').stream() # for only pendig orders
        orders = []

        
        for order in orders_ref:
            order_data = order.to_dict()  # Convert the document to a dictionary
            order_data['id'] = order.id  # Add the document ID to the order data
            orders.append(order_data)  # Append to the orders list
            
        return orders  # Return the list
    except Exception as e:
        print(f'Error fetching orders: {e}')
        return []  # Return an empty list if there was an error
    

def mark_order_comp(order_id):
    try:
        # get the product of order id provided          
        order_ref = db.collection('orders').document(order_id)

        # updating the status to Completed
        order_ref.update({
            'status': 'Completed'
        })

        return True
    except Exception as e:
        print(f"Error marking order complete: {e}")
        return False