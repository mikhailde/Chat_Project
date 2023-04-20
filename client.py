from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6 import QtCore
from UI import login, registration, ChatBox
from threading import Thread

import socket
import ssl


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations(cafile='TLS/server.crt')
serv = context.wrap_socket(sock, server_hostname='chatbox.ru')
try: serv.connect(('localhost', 25565))
except: exit()

class Login(QWidget, login.Ui_ChatBox):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label_2.installEventFilter(self)
        self.pushButton.clicked.connect(self.login)
        self.frame.setStyleSheet(stylesheet)
        

    def login(self):
        serv.send(':'.join(['login', self.lineEdit.text(), self.lineEdit_2.text()]).encode())
        status = serv.recv(1024).decode()
        print(status)
        if status == 'Error': self.label_3.setText('Неверные данные')
        else:
            serv.send(':'.join(['online', self.lineEdit.text()]).encode())
            self.close()
            main_window.show()

    def eventFilter(self, a0, a1) -> bool:
        
        if a1.type() == 2:
            btn = a1.button()
            if btn == QtCore.Qt.MouseButton.LeftButton:
                self.close()
                registration_window.show()
        return super().eventFilter(a0, a1)



class Registration(QWidget, registration.Ui_ChatBox):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label_2.installEventFilter(self)
        self.pushButton.clicked.connect(self.registration)
        self.frame.setStyleSheet(stylesheet)

    def registration(self):
        if self.lineEdit_2.text() != self.lineEdit_3.text(): self.label_3.setText('Пароли не совпадают')
        else:
            serv.send(':'.join(['register', self.lineEdit.text(), self.lineEdit_2.text()]).encode())
            status = serv.recv(1024).decode()
            print(status)
            if status == 'Error': self.label_3.setText('Ошибка')
            if status == 'Exists': self.label_3.setText('Уже зарегистрирован')
            else:
                serv.send(':'.join(['online', self.lineEdit.text()]).encode())
                self.close()
                main_window.show()

    def eventFilter(self, a0, a1) -> bool:
        
        if a1.type() == 2:
            btn = a1.button()
            if btn == QtCore.Qt.MouseButton.LeftButton:
                self.close()
                login_window.show()
        return super().eventFilter(a0, a1)
    
def message():
    while True:
            data = serv.recv(1024).decode().split(':')
            operation, *message = data
            if operation == 'online':
                count, *users = message
                main_window.label.setText("Участники: {} в сети".format(count))
                main_window.textEdit.setText('\n'.join(users))



class MainWindow(QMainWindow, ChatBox.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.action_3.triggered.connect(self.close)
        self.textBrowser.textChanged.connect(self.change)
        # self.changeText = 
        
    def change(self):
        self.textEdit.setText('\n'.join(self.users))

    def showEvent(self, event) -> None:
        
        th = Thread(target=self.message, daemon=True).start()

    def message(self):
        while True:
            data = serv.recv(1024).decode().split(':')
            operation, *message = data
            if operation == 'online':

                count, *users = message
                self.users = users
                self.label.setText("Участники: {} в сети".format(count))
                self.textBrowser.append('123')


class Message(QtCore.QThread):

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            data = serv.recv(1024).decode().split(':')
            operation, *message = data
            if operation == 'online':
                count, *users = message
                main_window.label.setText("Участники: {} в сети".format(count))
                # main_window.textEdit.setText('\n'.join(users))


    def stoped(self): 
        return self.working
        
        
    
        

    
    # def message(self):
    #     # serv.send(b'ready')
        
        


stylesheet = """
        background-image: url("UI/backlogo.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;
    
"""

if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    login_window = Login()
    registration_window = Registration()
    login_window.show()
    app.exec()
    serv.close()
    