from django.shortcuts import render

def category(request, category):
    # Fetch food items for the given category from the database or any data source
    # For simplicity, let's use a sample dictionary for now
    food_categories = {
    'breakfast': ['Pancakes', 'Omelette', 'French Toast', 'Waffles'],
    'veg-food': ['Vegetable Curry', 'Salad', 'Paneer Butter Masala', 'Mushroom Soup'],
    'non-veg-food': ['Chicken Wings', 'Fish Curry', 'Mutton Biryani', 'Chicken Tikka'],
    'fast-food': ['Burgers', 'Fries', 'Pizza', 'Sandwich'],
    'cold-drink': ['Coke', 'Pepsi', 'Lemonade', 'Iced Tea'],
    'desserts': ['Ice Cream', 'Cake', 'Brownies', 'Cupcakes']
    }

    items = food_categories.get(category, [])
    return render(request, 'category_page.html',{'category':category, 'food_items':items})

def menu(request):
    return render(request, 'menucard.html')