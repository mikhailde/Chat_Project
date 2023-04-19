from threading import Thread
import database as db

import socket
import ssl


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('localhost', 25565))
    sock.listen(10)
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile='TLS/server.crt', keyfile='TLS/server.key')
    ssl_sock = context.wrap_socket(sock, server_side=True)
    clients = set()


    def client_conn(conn):
        print('Connected')
        with conn:
            while True:
                data = conn.recv(1024).decode().split(':')
                if data: operation, username, password = data
                else: break
                print(operation)
                if operation == 'register':
                    if db.register(username, password): conn.send('Success'.encode())
                    else: conn.send('Exists'.encode())
                if operation == 'login':
                    if db.login(username, password): conn.send('Success'.encode())
                    else: conn.send('Error'.encode())
                # if operation == 'message':
                



    while True:
        conn, addr = ssl_sock.accept()
        clients.add(conn)
        client_thread = Thread(target=client_conn, args=[conn], daemon=True).start()
