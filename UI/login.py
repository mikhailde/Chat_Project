# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ChatBox(object):
    def setupUi(self, ChatBox):
        ChatBox.setObjectName("ChatBox")
        ChatBox.resize(240, 400)
        font = QtGui.QFont()
        font.setFamily("Arial")
        ChatBox.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/logo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        ChatBox.setWindowIcon(icon)
        ChatBox.setAutoFillBackground(False)
        ChatBox.setStyleSheet("")
        self.frame = QtWidgets.QFrame(parent=ChatBox)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(0, 0, 240, 400))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=ChatBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 200, 199, 31))
        self.lineEdit_2.setStatusTip("")
        self.lineEdit_2.setStyleSheet("border: 2px; border-radius: 10px;\n"
"background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setCursorPosition(0)
        self.lineEdit_2.setPlaceholderText("Пароль")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=ChatBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 350, 181, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_15.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setText("Регистрация")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_15.addWidget(self.label_2)
        self.pushButton = QtWidgets.QPushButton(parent=ChatBox)
        self.pushButton.setGeometry(QtCore.QRect(20, 250, 199, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(parent=ChatBox)
        self.lineEdit.setGeometry(QtCore.QRect(20, 160, 199, 31))
        self.lineEdit.setStyleSheet("border: 2px; border-radius: 10px;\n"
"background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("Имя пользователя")
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(ChatBox)
        QtCore.QMetaObject.connectSlotsByName(ChatBox)

    def retranslateUi(self, ChatBox):
        _translate = QtCore.QCoreApplication.translate
        ChatBox.setWindowTitle(_translate("ChatBox", "ChatBox - Вход"))
        self.frame.setStyleSheet(_translate("ChatBox", "0"))
        self.label.setText(_translate("ChatBox", "Нет аккаунта?"))
        self.pushButton.setText(_translate("ChatBox", "Войти"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChatBox = QtWidgets.QWidget()
    ui = Ui_ChatBox()
    ui.setupUi(ChatBox)
    ChatBox.show()
    sys.exit(app.exec())
