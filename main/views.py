from django.shortcuts import render, redirect
from django.contrib import messages
from .firebase import get_pending_orders, mark_order_comp, signup_user, login_user, store_order

def hotel_dashboard(request):
    orders = get_pending_orders()  # Fetch all orders from Firestore

    return render(request, 'hotel_dash.html', {'orders': orders})

def mark_order_complete(request, order_id):

    res = mark_order_comp(order_id)

    # Redirect the user back to the orders page
    return redirect('hotel_dashboard')


def category(request, category):
    # dummy data for food categories
    food_categories = {
    'breakfast': [
        {'name': 'Pancakes', 'image': 'https://images.unsplash.com/photo-1563805042-7684e1a34574?fit=crop&w=500&q=80'},
        {'name': 'Omelette', 'image': 'https://images.unsplash.com/photo-1572448862529-418ccf0e1c03?fit=crop&w=500&q=80'},
        {'name': 'French Toast', 'image': 'https://images.unsplash.com/photo-1570210714817-6c311aebf24c?fit=crop&w=500&q=80'},
        {'name': 'Waffles', 'image': 'https://images.unsplash.com/photo-1571091718763-95f35e03f0d4?fit=crop&w=500&q=80'}
    ],
    'veg-food': [
        {'name': 'Vegetable Curry', 'image': 'https://images.unsplash.com/photo-1606851093006-b66127301c89?fit=crop&w=500&q=80'},
        {'name': 'Salad', 'image': 'https://images.unsplash.com/photo-1572441714030-1cb11d6b1948?fit=crop&w=500&q=80'},
        {'name': 'Paneer Butter Masala', 'image': 'https://images.unsplash.com/photo-1628255769044-ef6ef90b27eb?fit=crop&w=500&q=80'},
        {'name': 'Mushroom Soup', 'image': 'https://images.unsplash.com/photo-1512058499757-0c9f28f78b84?fit=crop&w=500&q=80'}
    ],
    'non-veg-food': [
        {'name': 'Chicken Wings', 'image': 'https://images.unsplash.com/photo-1604908177543-679bcd88ed6b?fit=crop&w=500&q=80'},
        {'name': 'Fish Curry', 'image': 'https://images.unsplash.com/photo-1608730877435-4f308ba06b1f?fit=crop&w=500&q=80'},
        {'name': 'Mutton Biryani', 'image': 'https://images.unsplash.com/photo-1561452967-f4b1db0a17af?fit=crop&w=500&q=80'},
        {'name': 'Chicken Tikka', 'image': 'https://images.unsplash.com/photo-1592194996308-cbaf6f7e09c1?fit=crop&w=500&q=80'}
    ],
    'fast-food': [
        {'name': 'Burgers', 'image': 'https://images.unsplash.com/photo-1605646473538-79c222c5148a?fit=crop&w=500&q=80'},
        {'name': 'Fries', 'image': 'https://images.unsplash.com/photo-1586190848861-99aa4a171e90?fit=crop&w=500&q=80'},
        {'name': 'Pizza', 'image': 'https://images.unsplash.com/photo-1564936285084-edc221f9f23b?fit=crop&w=500&q=80'},
        {'name': 'Sandwich', 'image': 'https://images.unsplash.com/photo-1586190848863-b3d6ccca5a52?fit=crop&w=500&q=80'}
    ],
    'cold-drink': [
        {'name': 'Coke', 'image': 'https://images.unsplash.com/photo-1579960633382-8986c9ef32ce?fit=crop&w=500&q=80'},
        {'name': 'Pepsi', 'image': 'https://images.unsplash.com/photo-1594488018502-357fa2eb582b?fit=crop&w=500&q=80'},
        {'name': 'Lemonade', 'image': 'https://images.unsplash.com/photo-1626894767211-5fbb92e28c68?fit=crop&w=500&q=80'},
        {'name': 'Iced Tea', 'image': 'https://images.unsplash.com/photo-1598514983888-8879c582fa93?fit=crop&w=500&q=80'}
    ],
    'desserts': [
        {'name': 'Ice Cream', 'image': 'https://images.unsplash.com/photo-1532634726-8b9fb99845cd?fit=crop&w=500&q=80'},
        {'name': 'Cake', 'image': 'https://images.unsplash.com/photo-1599785209707-8af484b94a6c?fit=crop&w=500&q=80'},
        {'name': 'Brownies', 'image': 'https://images.unsplash.com/photo-1599781680115-9a307d41ef5b?fit=crop&w=500&q=80'},
        {'name': 'Cupcakes', 'image': 'https://images.unsplash.com/photo-1509529711801-deac231925ac?fit=crop&w=500&q=80'}
    ]
    }


    food_items = food_categories.get(category, [])
    return render(request, 'category_page.html', {
        'category': category,
        'food_items': food_items
    })

food_items_details = {
    'Pancakes': {
        'image': 'https://images.unsplash.com/photo-1563805042-7684e1a34574?fit=crop&w=500&q=80',
        'description': 'Fluffy pancakes served with syrup and butter.',
        'price': 150
    },
    'Omelette': {
        'image': 'https://images.unsplash.com/photo-1572448862529-418ccf0e1c03?fit=crop&w=500&q=80',
        'description': 'Delicious egg omelette stuffed with cheese and veggies.',
        'price': 120
    },
    'French Toast': {
        'image': 'https://images.unsplash.com/photo-1570210714817-6c311aebf24c?fit=crop&w=500&q=80',
        'description': 'Golden-brown French toast with a dash of cinnamon.',
        'price': 130
    },
    'Waffles': {
        'image': 'https://images.unsplash.com/photo-1571091718763-95f35e03f0d4?fit=crop&w=500&q=80',
        'description': 'Crispy waffles with a variety of toppings to choose from.',
        'price': 160
    },
    # Adding data for other food items...
}

def food_detail_view(request, food_name):
    # Fetch food details based on the name
    food_item = food_items_details.get(food_name, None)

    if food_item:
        return render(request, 'food_detail.html', {
            'food_name': food_name,
            'food_image': food_item['image'],
            'food_description': food_item['description'],
            'food_price': food_item['price']
        })
    else:
        return render(request, '404.html')

def menu(request):
    return render(request, 'menucard.html')


def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        address = request.POST.get('address')
        password = request.POST.get('password')

        check = request.POST.get('hotel_login')
        if(check == 'on'):
            hotel_login = True
        else:
            hotel_login = False


        user_id = signup_user(name, email, password, mobile, address, hotel_login)
        if user_id:
            messages.success(request, 'Signup successful! You can now login.')
            return redirect('login')  # Redirect to login URL
        else:
            messages.error(request, 'Signup failed. Please try again.')
            return render(request, 'signup.html')  # Retake the form

    return render(request, 'signup.html')  # Render the signup form if GET request


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Call the login_user function to verify the credentials
        user_info = login_user(email, password)

        if user_info:
            print('User logged in:', user_info)

            print('user logged in')
            request.session['user_uid'] = user_info['uid']
            request.session['user_data'] = user_info['data']  # Firestore user data
            #if (user_info['data'].get('hotel_login').isNotNull()):
            #    is_hotel_user = True

            is_hotel_user = user_info['data'].get('hotel_login', False)
            print('Is hotel user checked:', is_hotel_user)

            if is_hotel_user:
                messages.success(request, 'Login successful! Redirecting to hotel dashboard.')
                return redirect('hotel_dashboard')  # Redirect hotel users to a different page
            else:
                messages.success(request, 'Login successful! Redirecting to the main menu.')
                return redirect('menu')
        else:
            messages.error(request, 'Invalid email or password. Please try again.')
            return render(request, 'login.html')  # Show the login form again if login fails

    return render(request, 'login.html')  # Render the login form for GET requests


def buy_func(request):
    if 'user_uid' not in request.session:
        # Redirect to login if the user is not logged in
        messages.error(request, 'Please log in to proceed with the purchase.')
        return redirect('login')

    # Get the logged-in user's details
    user_uid = request.session['user_uid']
    user_data = request.session['user_data']  # Assuming the user data was stored in session during login

    if request.method == 'POST':
        # Extract the order details from the form or the page context
        food_name = request.POST.get('food_name')
        food_price = request.POST.get('food_price')
        food_description = request.POST.get('food_description')
        delivery_address = user_data.get('address')  # Using the user's stored address

        user_name = user_data.get('name')
        user_num = user_data.get('mobile')

        # Call the function to store the order in Firestore
        order_success = store_order(user_uid, food_name, food_price, food_description, delivery_address, user_name, user_num)

        if order_success:
            messages.success(request, 'Purchase successful! Your order will be delivered soon.')
            return redirect('menu')  # Redirect to the menu or another page after success
        else:
            messages.error(request, 'There was an issue processing your order. Please try again.')
            return redirect('buy')

    # Render the buy page if it's a GET request
    return render(request, 'buy.html')