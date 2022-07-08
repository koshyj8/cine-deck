# -*- coding: utf-8 -*-

################################################################################
# LogInWindow generated from reading UI file 'mainscreenAusfDX.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
import os
import PyQt5
from PyQt5 import QtWidgets, QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import mysql.connector as mc

from window_code.ui_signupscreen import Ui_SignUpWindow

from dotenv import load_dotenv
load_dotenv()

class Ui_LogInWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.selfsignupwindow = Ui_SignUpWindow()
        self.setupUi(self)

    def setupUi(self, LogInWindow):
        self.cursor_pix = QPixmap("CineDeck\assets\cursor.png")
        self.setStyleSheet("border-radius: 10px;")
        # 2. Scale textures
        self.cursor_scaled_pix = self.cursor_pix.scaled(
            QSize(40, 40), Qt.KeepAspectRatio)
        self.setStyleSheet(
            "background-color: rgba(175, 18, 90, 1); width: 0; ")
        # 3. Set cursor style and cursor focus position
        self.current_cursor = QCursor(self.cursor_scaled_pix, -1, -1)

        # 4. Set the cursor for the specified window
        LogInWindow.setCursor(self.current_cursor)
        LogInWindow.setWindowFlags(
            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMaximizeButtonHint)
        self.showMaximized()
        self.centralwidget = QWidget(LogInWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formWidget = QWidget(self.centralwidget)
        self.formWidget.setObjectName(u"formWidget")
        self.formWidget.setGeometry(QRect(130, 500, 800, 342))
        self.gridLayout = QGridLayout(self.formWidget)
        self.gridLayout.setSpacing(9)
        self.gridLayout.setContentsMargins(16, 16, 16, 16)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(3)
        self.passwordLineEdit = QLineEdit(self.formWidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setAutoFillBackground(True)
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        
        self.gridLayout.addWidget(self.passwordLineEdit, 1, 1, 1, 1)
        
        self.usernameLineEdit = QLineEdit(self.formWidget)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
        self.usernameLineEdit.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.gridLayout.addWidget(self.usernameLineEdit, 0, 1, 1, 1)

        self.usernameLabel = QLabel(self.formWidget)
        self.usernameLabel.setFont(QFont())
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.gridLayout.addWidget(self.usernameLabel, 0, 0, 1, 1)

        self.passwordLabel = QLabel(self.formWidget)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.gridLayout.addWidget(self.passwordLabel, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.formWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.formWidget)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(7)
        self.commandLinkButton.setFont(font)
        self.gridLayout.addWidget(self.commandLinkButton, 4, 1, 1, 1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(1000, 190, 1245,700))
        self.label_2.setPixmap(
            QPixmap(r"CineDeck\assets\movie posters\download.jpg"))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(17)
        self.label.setGeometry(390, 400, 600, 108)
        self.label.setFont(font1)
        self.label.setPixmap(
            QPixmap(r"CineDeck\assets\\logo.svg"))
        LogInWindow.setCentralWidget(self.centralwidget)
        self.usernameLineEdit.setStyleSheet("background-color: #fff8e7; border-radius: 10px")
        self.passwordLineEdit.setStyleSheet("background-color: #fff8e7; border-radius: 10px")
        self.pushButton.setStyleSheet(
            "background-color: #fff8e7; border-style: inset; border-width: 2px; border-color: black")
        self.statusbar = QStatusBar(LogInWindow)
        self.statusbar.setObjectName(u"statusbar")
        LogInWindow.setStatusBar(self.statusbar)
        
        self.poster_label = QLabel(self)
        self.poster_label.setObjectName(u"plabel")
        self.poster_label.setPixmap(
            QPixmap(r"CineDeck\assets\\download.svg"))
        self.poster_label.setGeometry(250, 235, 2400, 278)
        
        self.retranslateUi(LogInWindow)

        QMetaObject.connectSlotsByName(LogInWindow)

        self.pushButton.clicked.connect(self.login)
        self.commandLinkButton.clicked.connect(self.signupwindow)


    # setupUi

    def retranslateUi(self, LogInWindow):
        LogInWindow.setWindowTitle(QCoreApplication.translate(
            "LogInWindow", u"CineDeck - Log In", None))
        self.usernameLineEdit.setPlaceholderText(
            QCoreApplication.translate("LogInWindow", u"Enter Your Username", None))
        self.pushButton.setText(QCoreApplication.translate(
            "LogInWindow", u"Log In", None))
        self.passwordLabel.setText(QCoreApplication.translate(
            "LogInWindow", u"Password: ", None))
        self.passwordLineEdit.setText("")
        self.passwordLineEdit.setPlaceholderText(
            QCoreApplication.translate("LogInWindow", u"Enter Your Password", None))
        self.commandLinkButton.setText(QCoreApplication.translate(
            "LogInWindow", u"New to CineDeck? Sign Up!", None))
        self.usernameLabel.setText(QCoreApplication.translate(
            "LogInWindow", u"Username: ", None))
        self.label.setText("")
        self.poster_label.setText("")
    # retranslateUi

    def signupwindow(self):
        self.selfsignupwindow.setupUi(self)

    def login(self):
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()
        if username and password is not None:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password=os.getenv('mysqlpass'),
                database="cinedeck")

            mycursor = mydb.cursor()
            query = "SELECT username,pass from user_info where username " \
                    "like '"+username + "'and pass like '" \
                    + password + "'"
            mycursor.execute(query)
            result = mycursor.fetchone()

            if result == None:
                QtWidgets.QMessageBox.critical(
                    self, "Error", "Username or password is incorrect!")

            else:
                QtWidgets.QMessageBox.information(
                    self, "Success ✅", "You Have Been Logged In!")
                self.mainscreen
        else:
            QtWidgets.QMessageBox.information(
                self, "Error ", "Please Enter Username or Password.")

    def mainscreen(self):
        self.selfmainscreen.setupUi(self)

if __name__ == "__main__":
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    ex = Ui_LogInWindow()
    ex.show()
    sys.exit(app.exec_())
