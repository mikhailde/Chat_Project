from threading import Thread
import database as db

import socket
import ssl


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('localhost', 25565))
    sock.listen(10)
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile='TLS/server.crt', keyfile='TLS/server.key')
    ssl_sock = context.wrap_socket(sock, server_side=True)
    clients = set()


    def client_conn(conn):
        global clients
        print('Connected')
        with conn:
            while True:
                data = conn.recv(1024).decode().split(':')
                if data != ['']: operation, *message = data
                else:
                    
                    clients.remove((conn,username))
                    for client in clients: client[0].send(':'.join(['online', str(len(clients)), ':'.join([client[1] for client in clients])]).encode())

                    break
                if operation == 'register':
                    username, password = message
                    if db.register(*message): conn.send(b'Success')
                    else: conn.send('Exists'.encode())
                if operation == 'login':
                    username, password = message
                    if db.login(*message):
                        conn.send(b'Success')
                    else: conn.send('Error'.encode())
                if operation == 'online':
                    clients.add((conn, *message))
                    for client in clients: client[0].send(':'.join(['online', str(len(clients)), ':'.join([client[1] for client in clients])]).encode())

                    
                # if operation == 'message':
                



    while True:
        conn, addr = ssl_sock.accept()
        client_thread = Thread(target=client_conn, args=[conn], daemon=True).start()
