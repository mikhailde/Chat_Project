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
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print('Connected by', addr)
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            decrypted_data = decrypt_message(data, KEY)
            print(decrypted_data)
            message = input('Enter your message: ')
            encrypted_message = encrypt_message(message, KEY)
            conn.sendall(encrypted_message)
