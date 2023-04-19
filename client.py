from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt6 import QtCore
from UI import login, registration, ChatBox

import socket
import ssl


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations(cafile='TLS/server.crt')
serv = context.wrap_socket(sock, server_hostname='chatbox.ru')
serv.connect(('localhost', 25565))

class Login(QWidget, login.Ui_ChatBox):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.label_2.installEventFilter(self)
        self.pushButton.clicked.connect(self.login)
        self.frame.setStyleSheet(stylesheet)
        

    def login(self):
        print(':'.join(['login', self.lineEdit.text(), self.lineEdit_2.text()]).encode())
        serv.send(':'.join(['login', self.lineEdit.text(), self.lineEdit_2.text()]).encode())
        status = serv.recv(1024).decode()
        print(status)
        if status == 'Error': self.label_3.setText('Неверные данные')
        else: self.close()

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
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.label_2.installEventFilter(self)
        self.pushButton.clicked.connect(self.registration)
        self.frame.setStyleSheet(stylesheet)

    def registration(self):
        if self.lineEdit_2.text() != self.lineEdit_3.text(): self.label_3.setText('Пароли не совпадают')
        else:
            print(':'.join(['register', self.lineEdit.text(), self.lineEdit_2.text()]).encode())
            serv.send(':'.join(['register', self.lineEdit.text(), self.lineEdit_2.text()]).encode())
            status = serv.recv(1024).decode()
            print(status)
            if status == 'Error': self.label_3.setText('Ошибка')
            if status == 'Exists': self.label_3.setText('Уже зарегистрирован')
            else: self.close()

    def eventFilter(self, a0, a1) -> bool:
        
        if a1.type() == 2:
            btn = a1.button()
            if btn == QtCore.Qt.MouseButton.LeftButton:
                self.close()
                login_window.show()
        return super().eventFilter(a0, a1)
    


class MainWindow(QMainWindow, ChatBox.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.action_3.triggered.connect(self.close)
        


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
    main_window.show()
    login_window.show()
    app.exec()
    serv.close()
    