import sqlite3
from pass_hash import hash_password

def login_user(username, password):
    # Хэширование пароля
    hashed_password = hash_password(password)
    # Проверка, что пользователь с таким именем существует
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    if user is None:
        print(f'User {username} not found')
        return False
    # Проверка, что введенный пароль совпадает с хэшированным паролем из базы данных
    if user[2] != hashed_password:
        print(f'Invalid password for user {username}')
        return False
    cursor.close()
    conn.close()
    print(f'User {username} logged in successfully')
    return True
