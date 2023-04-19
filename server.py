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
        with conn:
            while True:
                operation, username, password = conn.recv(1024).decode().split(':')
                if operation == 'login':



    while True:
        conn, addr = ssl_sock.accept()
        clients.append(conn)
        client_thread = Thread(target=client_conn, args=(conn))



        data = conn.recv(1024)
        print(data)

        conn.send(b'Hello')

        conn.close()