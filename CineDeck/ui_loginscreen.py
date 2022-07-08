import sys
import os
import PyQt5
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import mysql.connector as mc
from qtwidgets import PasswordEdit



class Ui_LogInWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def signupwindow(self):
        self.selfsignupwindow.setupUi()

    def setupUi(self, LogInWindow):
        self.cursor_pix = QPixmap("assets\cursor.png")

        # 2. Scale textures
        self.cursor_scaled_pix = self.cursor_pix.scaled(
            QSize(40, 40), Qt.KeepAspectRatio)

        # 3. Set cursor style and cursor focus position
        self.current_cursor = QCursor(self.cursor_scaled_pix, -1, -1)

        # 4. Set the cursor for the specified window
        LogInWindow.setCursor(self.current_cursor)
        LogInWindow.resize(696, 358)
        self.centralwidget = QWidget(LogInWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.loginwindowWidget = QWidget(self.centralwidget)
        self.loginwindowWidget.setObjectName(u"loginwindowWidget")
        self.loginwindowWidget.setGeometry(QRect(170, 70, 481, 201))
        self.gridLayout = QGridLayout(self.loginwindowWidget)
        self.gridLayout.setSpacing(9)
        self.gridLayout.setContentsMargins(16, 16, 16, 16)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(3)
        self.radioButton = QRadioButton(self.loginwindowWidget)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout.addWidget(self.radioButton, 2, 0, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.loginwindowWidget)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(7)
        self.commandLinkButton.setFont(font)

        self.gridLayout.addWidget(self.commandLinkButton, 3, 1, 1, 1)

        self.usernameLabel = QLabel(self.loginwindowWidget)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.gridLayout.addWidget(self.usernameLabel, 0, 0, 1, 1)

        self.passwordLabel = QLabel(self.loginwindowWidget)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.gridLayout.addWidget(self.passwordLabel, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.loginwindowWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)

        self.usernameLineEdit = QLineEdit(self.loginwindowWidget)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
        self.usernameLineEdit.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.gridLayout.addWidget(self.usernameLineEdit, 0, 1, 1, 1)

        self.passwordLineEdit = QLineEdit(self.loginwindowWidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setAutoFillBackground(False)
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.passwordLineEdit, 1, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 40, 91, 45))
        font1 = QFont()
        font1.setPointSize(17)
        self.label.setFont(font1)
        LogInWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(LogInWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 696, 22))
        self.menuLog_I = QMenu(self.menubar)
        self.menuLog_I.setObjectName(u"menuLog_I")
        LogInWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(LogInWindow)
        self.statusbar.setObjectName(u"statusbar")
        LogInWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuLog_I.menuAction())
        self.menuLog_I.addSeparator()
        self.menuLog_I.addSeparator()

        self.retranslateUi(LogInWindow)

        QMetaObject.connectSlotsByName(LogInWindow)
    # setupUi

        self.pushButton.clicked.connect(self.login)
        self.commandLinkButton.clicked.connect(self.signupwindow)
        self.labelResult = QtWidgets.QLabel(LogInWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelResult.setFont(font)
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")

        self.retranslateUi(LogInWindow)
        QtCore.QMetaObject.connectSlotsByName(LogInWindow)


    def login(self):
        try:
            email = self.usernameLineEdit.text()
            password = self.passwordLineEdit.text()
            if email or password is None:
                self.labelResult.setText("Please enter username and password.")
            else:                
                mydb = mc.connect(
                    host="localhost",
                    user="root",
                    password=os.getenv('mysqlpass'),
                    database="")

                mycursor = mydb.cursor()
                query = "SELECT email,password from users where email " \
                        "like '"+email + "'and password like '" \
                        + password + "'"
                mycursor.execute(query)
                result = mycursor.fetchone()

                if result == None:
                    self.labelResult.setText("Incorrect email or password")

                else:
                    self.labelResult.setText("You are logged in")
                    mydialog = QDialog()
                    mydialog.setModal(True)
                    mydialog.exec_()

        except mc.Error as e:
            self.labelResult.setText("Error")

    def retranslateUi(self, LogInWindow):
        LogInWindow.setWindowTitle(QCoreApplication.translate(
            "LogInWindow", u"MainWindow", None))
        self.radioButton.setText(QCoreApplication.translate(
            "LogInWindow", u"Remember Me?", None))
        self.commandLinkButton.setText(QCoreApplication.translate(
            "LogInWindow", u"New to CineDeck? Sign Up!", None))
        self.usernameLabel.setText(QCoreApplication.translate(
            "LogInWindow", u"Username: ", None))
        self.passwordLabel.setText(QCoreApplication.translate(
            "LogInWindow", u"Password: ", None))
        self.pushButton.setText(QCoreApplication.translate(
            "LogInWindow", u"Log In", None))
        self.usernameLineEdit.setPlaceholderText(
            QCoreApplication.translate("LogInWindow", u"Enter Your Username", None))
        self.passwordLineEdit.setText("")
        self.passwordLineEdit.setPlaceholderText(
            QCoreApplication.translate("LogInWindow", u"Enter Your Password", None))
        self.label.setText(QCoreApplication.translate(
            "LogInWindow", u"CineDeck", None))
        self.menuLog_I.setTitle(QCoreApplication.translate(
            "LogInWindow", u"Log In", None))
    # retranslateUi
