"""Модули для захвата сигналов, сокетов, шифрования, потоков, и базы данных"""
import signal
import socket
import ssl
import sys
import argparse

from threading import Thread

import database as db


def get_ip():
	with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
		s.connect(('8.8.8.8',80))
		return s.getsockname()[0]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    parser = argparse.ArgumentParser(description='A tutorial of argparse!')
    parser.add_argument('--host', default=get_ip(), type=str, help="Host IP address")
    parser.add_argument('--port', default=25565, type=int, help="Host port")
    args = parser.parse_args()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((args.host, args.port))
    sock.listen(10)
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile='TLS/server.crt', keyfile='TLS/server.key')
    ssl_sock = context.wrap_socket(sock, server_side=True)
    print(f'Server started at {args.host}, {args.port}')
    clients = set()


    def client_conn(conn, addr):
        """Функция подключения клиента"""
        global clients
        print(f'Connected {addr}')
        with conn:
            while True:
                data = conn.recv(1024).decode().split(':')
                print(data)
                if data != ['']:
                    operation, *message = data
                else:
                    operation = 'logout'
                if operation == 'register':
                    username = message[0]
                    if db.register(*message):
                        conn.sendall(b'Success')
                    else:
                        conn.sendall(b'Exists')
                if operation == 'login':
                    username = message[0]
                    if username in [client[1] for client in clients]:
                        conn.sendall(b'Used')
                    elif db.login(*message):
                        conn.sendall(b'Success')
                    else:
                        conn.sendall(b'Error')
                if operation == 'online':
                    clients.add((conn, *message))
                    for client in clients:
                        client[0].sendall(':'.join(['online', str(len(clients)), ':'.join([client[1] for client in clients])]).encode())
                if operation == 'logout':
                    if data == ['']:
                        print(f'Disconnected {addr}')
                        break
                    conn.sendall(b'logout')
                    clients.remove((conn,username))
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
        sys.exit()

    signal.signal(signal.SIGINT, stop_server)

    while True:
        conn, addr = ssl_sock.accept()
        Thread(target=client_conn, args=[conn, addr], daemon=True).start()
