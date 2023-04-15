import socket
import threading
import hashlib

HOST = '127.0.0.1'
PORT = 65432
BUFF_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def register_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    s.send(f"REGISTER:{username}:{password}".encode())
    response = s.recv(BUFF_SIZE).decode()
    if response == "SUCCESS":
        print("Registration successful!")
    else:
        print("Registration failed. User already exists.")

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    s.send(f"LOGIN:{username}:{password}".encode())
    response = s.recv(BUFF_SIZE).decode()
    if response == "SUCCESS":
        print("Login successful!")
        return username
    else:
        print("Login failed. Invalid username or password.")
        return None

def logout_user():
    s.send("LOGOUT".encode())

def send_message():
    while True:
        message = input("Enter your message: ")
       
