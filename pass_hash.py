import hashlib

def hash_password(password):
    salt = b'some_random_salt'
    # Добавление соли к паролю
    salted_password = password.encode('utf-8') + salt
    # Хэширование пароля
    hashed_password = hashlib.sha256(salted_password).hexdigest()
    return hashed_password
