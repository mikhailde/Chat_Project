"""Шифрование, сокеты и UI"""
import socket
import ssl
import argparse

from threading import Thread
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6 import QtCore
from UI import login, registration, ChatBox


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations(cafile='TLS/server.crt')
serv = context.wrap_socket(sock, server_hostname='chatbox.ru')
parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument('--host', default='185.107.237.242', type=str, help="Host IP address")
parser.add_argument('--port', default=25565, type=int, help="Host port")
args = parser.parse_args()
try:
    serv.connect((args.host, args.port))
except Exception as e:
    print('Сервер недоступен')


class Login(QWidget, login.Ui_ChatBox):
    """Окно входа"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label_2.installEventFilter(self)
        self.pushButton.clicked.connect(self.login)

    def keyPressEvent(self, e) -> None:
        """Метода захвата нажатия на Enter"""
        if e.key() == 16777220:
            self.login()
        return super().keyPressEvent(e)

    def login(self):
        """Метод входа"""
        if not self.lineEdit.text() and not self.lineEdit_2.text():
            self.label_3.setText('Заполните все поля')
        else:
            serv.sendall(':'.join(['login', self.lineEdit.text(), self.lineEdit_2.text()]).encode())
            status = serv.recv(1024)
            if status.decode() == 'Error':
                self.label_3.setText('Неверные данные')
            if status.decode() == 'Used':
                self.label_3.setText('Аккаунт уже используется')
            else:
                serv.sendall(':'.join(['online', self.lineEdit.text()]).encode())
                self.close()
                main_window.show()

    def eventFilter(self, a0, a1) -> bool:
        """Захват нажатия на кнопку регистрации"""
        if a1.type() == 2:
            btn = a1.button()
            if btn == QtCore.Qt.MouseButton.LeftButton:
                self.close()
                registration_window.show()
        return super().eventFilter(a0, a1)



class Registration(QWidget, registration.Ui_ChatBox):
    """Окно регистрации"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label_2.installEventFilter(self)
        self.pushButton.clicked.connect(self.registration)

    def keyPressEvent(self, e) -> None:
        """Метода захвата нажатия на Enter"""
        if e.key() == 16777220:
            self.registration()
        return super().keyPressEvent(e)

    def registration(self):
        """Метод регистрации"""
        if not self.lineEdit.text() and not self.lineEdit_2.text() and not self.lineEdit_3.text():
            self.label_3.setText('Заполните все поля')
        elif self.lineEdit_2.text() != self.lineEdit_3.text():
            self.label_3.setText('Пароли не совпадают')
        else:
            serv.sendall(':'.join(['register', self.lineEdit.text(), self.lineEdit_2.text()]).encode())
            status = serv.recv(1024).decode()
            print(status)
            if status == 'Error':
                self.label_3.setText('Ошибка')
            if status == 'Exists':
                self.label_3.setText('Аккаунт уже зарегистрирован')
            else:
                serv.sendall(':'.join(['online', self.lineEdit.text()]).encode())
                self.close()
                main_window.show()

    def eventFilter(self, a0, a1) -> bool:
        """Захват нажатия на кнопку входа"""
        if a1.type() == 2:
            btn = a1.button()
            if btn == QtCore.Qt.MouseButton.LeftButton:
                self.close()
                login_window.show()
        return super().eventFilter(a0, a1)


class MainWindow(QMainWindow, ChatBox.Ui_MainWindow):
    """Окно чата"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.action_3.triggered.connect(self.close)
        self.action_2.triggered.connect(self.logout)
        self.textBrowser.textChanged.connect(self.change)
        self.pushButton_2.clicked.connect(self.send_message)
        self.textEdit_2.toHtml()

    def logout(self):
        """Метод выхода из аккаунта"""
        self.close()
        serv.sendall(b'logout')
        login_window.show()
        

    def send_message(self):
        """Метод отправки сообщения"""
        if self.lineEdit_3.text():
            serv.sendall(':'.join(['message', self.lineEdit_3.text()]).encode())
            self.textEdit_2.append('')
            self.textEdit_2.insertHtml(f'<p align="right" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:11pt;">{self.lineEdit_3.text()}</span></p>')
            self.textEdit_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
            self.lineEdit_3.clear()

    def change(self):
        """Метод изменения списка участников"""
        self.textEdit.setText('\n'.join(self.users))

    def showEvent(self, event) -> None:
        """Метод запускающий метод приема сообщений при запуске приложения"""
        Thread(target=self.message, daemon=True).start()

    def keyPressEvent(self, e) -> None:
        """Метода захвата нажатия на Enter"""
        if e.key() == 16777220:
            self.send_message()
        return super().keyPressEvent(e)

    def message(self):
        """Метод приема сообщений"""
        while True:
            data = serv.recv(1024).decode().split(':')
            print(data)
            if data != ['']: operation, *message = data
            else:
                self.close()
                break
            if operation == 'online':
                count, *users = message
                self.users = users
                self.label.setText("Участники: {} в сети".format(count))
                self.textBrowser.append('123')
            if operation == 'logout':
                break
            if operation == 'message':
                username, message = message
                self.textEdit_2.append('')
                self.textEdit_2.insertHtml(f'<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:11pt; font-weight:600;">{username}:</span><span style=" font-size:11pt;"> {message}</span></p>')
                self.textEdit_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)



if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    login_window = Login()
    registration_window = Registration()
    login_window.show()
    app.exec()
    serv.close()
    
