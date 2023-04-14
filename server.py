import socket
import threading
import hashlib

HOST = '127.0.0.1'
PORT = 65432
BUFF_SIZE = 1024

def handle_client(conn, addr):
    print(f"New connection from {addr}")
    while True:
        data = conn.recv(BUFF_SIZE)
        if not data:
            break
        hashed_message = hashlib.sha256(data).hexdigest()
        print(f"Received message from {addr}: {hashed_message}")
        conn.send(hashed_message.encode())
    print(f"Connection from {addr} closed")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server started on {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()
