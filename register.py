import sqlite3
from pass_hash import hash_password

def register_user(username, password):
    # Хэширование пароля
    hashed_password = hash_password(password)
    # Проверка, что пользователь с таким именем еще не зарегистрирован
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    if cursor.fetchone() is not None:
        print(f'User {username} already exists')
        return False
    # Добавление нового пользователя в базу данных
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
    conn.commit()
    cursor.close()
    conn.close()
    print(f'User {username} registered successfully')
    return True
