import json

# Function to load data from database.json
def load_database_data():
    file_name = "database.json"
    with open(file_name, "r", encoding="utf-8") as json_file:
        return json.load(json_file)

# Function to save data to database.json
def save_database_data(data):
    file_name = "database.json"
    with open(file_name, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)

# Function to check if a user exists based on user_id
def user_exists(user_id):
    data = load_database_data()
    for user in data['users']:
        if user['user_id'] == user_id:
            return True
    return False

# Function to add a new user to the database
def add_user(user_id, active=True):
    data = load_database_data()
    new_user = {
        "id": len(data['users']) + 1,
        "user_id": user_id,
        "active": active
    }
    data['users'].append(new_user)
    save_database_data(data)

# Function to set active status for a user
def set_active(user_id, active):
    data = load_database_data()
    for user in data['users']:
        if user['user_id'] == user_id:
            user['active'] = active
            save_database_data(data)
            return True
    return False

# Function to get users based on user_id and active status
def get_users(user_id=None, active=None):
    data = load_database_data()
    filtered_users = []

    for user in data['users']:
        if (user_id is None or user['user_id'] == user_id) and \
           (active is None or user['active'] == active):
            filtered_users.append(user)

    return filtered_users