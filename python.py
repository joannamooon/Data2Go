# Predefined data
user_data = [
    {
        "First Name": "John",
        "Last Name": "Doe",
        "Birthdate": "2006-01-01",
        "Address": "123 Main St",
        "Children Count": 2,
        "Income Range": "30,000-50,000",
        "Housing Type": "Own Home",
        "Dietary Restrictions": "None",
        "Weekly Needs": ["fruit", "vegetables", "protein", "grains", "dairy"]
    },
    {
        "First Name": "Jane",
        "Last Name": "Smith",
        "Birthdate": "2007-03-15",
        "Address": "456 Oak Ave",
        "Children Count": 1,
        "Income Range": "10,000-30,000",
        "Housing Type": "Private Rental",
        "Dietary Restrictions": "Vegetarian",
        "Weekly Needs": ["fruit", "vegetables", "grains"]
    },
    {
        "First Name": "Bob",
        "Last Name": "Johnson",
        "Birthdate": "2009-07-20",
        "Address": "789 Elm Rd",
        "Children Count": 3,
        "Income Range": "70,000+",
        "Housing Type": "Own Home",
        "Dietary Restrictions": "Gluten-Free",
        "Weekly Needs": ["protein", "grains", "dairy"]
    },
    {
        "First Name": "Emily",
        "Last Name": "Davis",
        "Birthdate": "2010-12-10",
        "Address": "101 Pine Ln",
        "Children Count": 0,
        "Income Range": "30,000-50,000",
        "Housing Type": "Social Housing",
        "Dietary Restrictions": "Vegan",
        "Weekly Needs": ["fruit", "vegetables"]
    },
    {
        "First Name": "Michael",
        "Last Name": "Brown",
        "Birthdate": "2016-05-05",
        "Address": "202 Maple Dr",
        "Children Count": 2,
        "Income Range": "10,000-30,000",
        "Housing Type": "Emergency Shelter",
        "Dietary Restrictions": "Nut-Free",
        "Weekly Needs": ["grains", "dairy"]
    }
]

food_inventory = {
    "fruit": {
        "Apples": 5,
        "Bananas": 3,
    },
    "vegetables": {
        "Carrots": 3,
    },
    "protein": {
        "Chicken (in lbs)": 10,
        "Eggs (dozen)": 30,
    },
    "grains": {
        "Rice (in lbs)": 15,
        "Pasta (in lbs)": 20,
    },
    "dairy": {
        "Milk (in gallons)": 4,
        "Cheese (in lbs)": 2,
    },
}

# Initialize food groups in user data
def initialize_food_groups(user_data):
    for user in user_data:
        for group in food_inventory:
            for item in food_inventory[group]:
                user[item] = 0

initialize_food_groups(user_data)

def distribute_food_to_users(user_data, food_inventory):
    distributed_data = []  # List to store distributed user data

    for user in user_data:
        user_needs = user["Weekly Needs"]
        distributed_user = user.copy()  # Create a copy of the user data

        unmet_needs = []  # Create a list to track unmet needs

        for need in user_needs:
            if need in food_inventory:  # Check if the need is a food group
                food_group = need
                for food_item, quantity in food_inventory[food_group].items():
                    if quantity > 0:
                        distributed_quantity = min(distributed_user["Children Count"], quantity)
                        distributed_user[food_item] += distributed_quantity
                        food_inventory[food_group][food_item] -= distributed_quantity
                        if quantity - distributed_quantity > 0:
                            # If there are unmet needs within the group, add the need back to unmet_needs
                            unmet_needs.append(need)
            else:
                # If the need is not found in food_inventory, add it to unmet_needs
                unmet_needs.append(need)

        # Update the user's unmet needs
        user["Weekly Needs"] = unmet_needs

        distributed_data.append(distributed_user)

    return distributed_data




distributed_user_data = distribute_food_to_users(user_data, food_inventory)

def get_specific_foods(user, food_inventory):
    specific_foods = []
    for group in food_inventory:
        for food_item, quantity in food_inventory[group].items():
            if quantity > 0 and user.get(food_item, 0) > 0:
                specific_foods.append(food_item)
    return specific_foods

# Print the specific food items needed
for user in distributed_user_data:
    first_name = user['First Name']
    last_name = user['Last Name']
    specific_foods = get_specific_foods(user, food_inventory)
    if specific_foods:
        print(f"{first_name} {last_name} needs: {', '.join(specific_foods)}")

