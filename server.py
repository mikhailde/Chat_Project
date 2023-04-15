import socket
import threading
import hashlib
import sqlite3

HOST = '127.0.0.1'
PORT = 65432
BUFF_SIZE = 1024

conn = sqlite3.connect('users.sql')
c = conn.cursor()

def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                (username TEXT, password TEXT, status TEXT)''')
    conn.commit()

def register_user(username, password):
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    user = c.fetchone()
    if user:
        return False
    else:
        c.execute("INSERT INTO users (username, password, status) VALUES (?, ?, ?)",
                  (username, password, 'inactive'))
        conn.commit()
        return True

def login_user(username, password):
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    if user:
        c.execute("UPDATE users SET status='active' WHERE username=?", (username,))
        conn.commit()
        return True
    else:
        print("You don't have an account. Register now.")
        register_user(username, password)
        return True

def logout_user(username):
    c.execute("UPDATE users SET status='inactive' WHERE username=?", (username,))
    conn.commit()

def get_active_users():
    c.execute("SELECT username FROM users WHERE status='active'")
    users = c.fetchall()
    return [user[0] for user in users]

def handle_client(conn, addr):
    create_table()
    print(f"New connection from {addr}")
    while True:
        data = conn.recv(BUFF_SIZE)
        if not data:
            break
        username, message = data.decode().split(":")
        hashed_message = hashlib.sha256(message.encode()).hexdigest()
        print(f"Received message from {username}: {hashed_message}")
        active_users = get_active_users()
        for client in clients:
            if client != conn and client in active_users:
                client.send(f"{username}: {message}".encode())
        conn.send(hashed_message.encode())
    username = conn.username
    logout_user(username)
    print(f"Connection from {addr} closed")

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server started on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

clients = []

start_server()
