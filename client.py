import socket
import hashlib

HOST = '127.0.0.1'
PORT = 65432
BUFF_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input("Enter your message: ")
        hashed_message = hashlib.sha256(message.encode()).hexdigest()
        s.send(hashed_message.encode())
        data = s.recv(BUFF_SIZE)
        decrypted_data = data.decode()
        print(f"Received message from server: {decrypted_data}")
