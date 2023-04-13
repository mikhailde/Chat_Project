import socket
from cryptography.fernet import Fernet

HOST = '127.0.0.1'
PORT = 65432
KEY = Fernet.generate_key()

def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input('Enter your message: ')
        encrypted_message = encrypt_message(message, KEY)
        s.sendall(encrypted_message)
        data = s.recv(1024)
        decrypted_data = decrypt_message(data, KEY)
        print(decrypted_data)
