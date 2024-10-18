# Варіант 2: Redis (ключ-значення)
# 1. Збереження сесій користувачів:
# Створіть просту модель сесій користувачів для веб-додатку, використовуючи Redis для зберігання стану користувачів.
# Наприклад, зберігайте такі дані: user_id, session_token, login_time.
# 2. CRUD операції:#
# • Create: Додайте нову сесію для користувача.
# • Read: Отримайте активну сесію для конкретного користувача.
# • Update: Оновіть час останньої активності користувача.
# • Delete: Видаліть сесію після виходу користувача з системи.
# 3. TTL (Time to Live):
# Налаштуйте час життя сесії користувача. Автоматично видаляйте сесію, якщо користувач не активний більше 30 хвилин.

import redis # A library that provides an interface to interact with the Redis database (key-value format).
from datetime import datetime # To work with date and time.

# Create an object (connection to the Redis database).
client = redis.Redis(host='localhost', port=6379, db=0)
# host=‘localhost’: specify that the Redis server is located locally.
# port=6379: the default port for Redis.
# db=0: Redis supports multiple databases. The first database (with index 0) is used here.

# ***Create***
def create_session(user_id, session_token):
    '''
    Creates a new session for the user.
    :param user_id:  User ID (unique key).
    :param session_token: generated upon successful user authorisation.
    '''
    # Get the user's login time
    login_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # datetime.now(): get the current time.
    # strftime('%Y-%m-%d %H:%M:%S'): format the current time into a string in the format YYYYY-MM-DD HH:MM:SS

    # Create a session_data dictionary that contains information about the session.
    session_data = {
        'session_token': session_token, # Storing the session token.
        'login_time': login_time, # The time of login.
        'last_active_time': login_time # The time of the user's last activity (== login_time, when the session is created).
    }

    # Add each key and value.
    for key, value in session_data.items():
        client.hset(f"user_session:{user_id}", key, value)
        # hset: adds the field and its value to the hash in Redis
        # session_data = {
        #     'session_token': 'abc123xyz',
        #     'login_time': '2024-10-10 10:00:00',
        #     'last_active_time': '2024-10-10 10:00:00'
        # }

    # Set the time to live (TTL) for the user session.
    client.expire(f"user_session:{user_id}", 1800)  # 1800 seconds = 30 minutes
    # expire: sets the time in seconds.

# ***Read***
def get_session(user_id):
    '''Retrieves the active session data for the specified user.'''
    session_data = client.hgetall(f"user_session:{user_id}")
    # hgetall: to retrieve all hash data for the user with user_id.
    # The method returns all fields and values associated with this user as a byte dictionary.

    # Check if the session data has been received
    if session_data:
        # Return a dictionary with session data.
        return {key.decode(): value.decode() for key, value in session_data.items()}
        # decode(): decode keys and values from bytes to strings.
    else:
        return None

# ***Update***
def update_last_active_time(user_id):
    '''Updates the time of the user's last activity.'''
    # Get the current time and format it as a string in YYYYY-MM-DD HH:MM:SS format to update the user's activity time.
    last_active_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Check if a session exists.
    if client.exists(f"user_session:{user_id}"):
        # Update the last_active_time field in the user session hash. Now it stores the new last activity time.
        client.hset(f"user_session:{user_id}", 'last_active_time', last_active_time)
        # Update TTL when the user is active (again 30 minutes)
        client.expire(f"user_session:{user_id}", 1800)
        print(f"Time of last activity for {user_id} is updated.")
    else:
        print(f"No session found for {user_id}.")

# ***Delete***
def delete_session(user_id):
    '''Deletes the user session.'''
    client.delete(f"user_session:{user_id}")
    print(f"Session for {user_id} was deleted.")


# Testing:
create_session('user123', 'abc123xyz')
update_last_active_time('user123')
delete_session('user123')
