"""Модули для захвата сигналов, сокетов, шифрования, потоков, и базы данных"""
import signal
import socket
import ssl

from threading import Thread

import database as db


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('localhost', 25565))
    sock.listen(10)
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile='TLS/server.crt', keyfile='TLS/server.key')
    ssl_sock = context.wrap_socket(sock, server_side=True)
    print('Server started')
    clients = set()


    def client_conn(conn, addr):
        """Функция подключения клиента"""
        global clients
        print('Connected')
        with conn:
            while True:
                data = conn.recv(1024).decode().split(':')
                if data != ['']:
                    operation, *message = data
                else:
                    try:
                        clients.remove((conn,username))
                        for client in clients:
                            client[0].sendall(':'.join(['online', str(len(clients)), ':'.join([client[1] for client in clients])]).encode())
                    except Exception as e:
                        print(e)
                    print(f'Disconnected {addr}')
                    break
                if operation == 'register':
                    username = message[0]
                    if db.register(*message):
                        conn.sendall(b'Success')
                    else:
                        conn.sendall(b'Exists')
                if operation == 'login':
                    username = message[0]
                    if db.login(*message):
                        conn.sendall(b'Success')
                    else:
                        conn.sendall('Error'.encode())
                if operation == 'online':
                    clients.add((conn, *message))
                    for client in clients:
                        client[0].sendall(':'.join(['online', str(len(clients)), ':'.join([client[1] for client in clients])]).encode())
                if operation == 'message':
                    for client in clients:
                        if client[0] != conn:
                            client[0].sendall(':'.join(['message', username, *message]).encode())

    def stop_server(sig, frame):
        """Метод остановки сервера"""
        print('Server stopped')
        clients.clear()
        sock.close()
        exit()

    signal.signal(signal.SIGINT, stop_server)

    while True:
        conn, addr = ssl_sock.accept()
        print(f'Connected {addr}')
        Thread(target=client_conn, args=[conn, addr], daemon=True).start()
