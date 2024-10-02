from django.shortcuts import render, redirect
from django.contrib import messages
from .firebase import signup_user, login_user

def category(request, category):
    # Fetch food items for the given category from the database or any data source
    # For simplicity, let's use a sample dictionary for now
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

        user_id = signup_user(email, password, mobile, address)
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
            # Store user information in session
            request.session['user_uid'] = user_info['uid']
            request.session['user_data'] = user_info['data']  # Firestore user data

            messages.success(request, 'Login successful!')
            return redirect('menu')  # Redirect to menu if successfull login
        else:
            messages.error(request, 'Invalid email or password. Please try again.')
            return render(request, 'login.html')  # Show the login form again if login fails

    return render(request, 'login.html')  # Render the login form for GET requests