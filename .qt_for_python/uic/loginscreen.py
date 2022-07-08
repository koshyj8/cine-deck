# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginscreen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LogInWindow(object):
    def setupUi(self, LogInWindow):
        if not LogInWindow.objectName():
            LogInWindow.setObjectName(u"LogInWindow")
        LogInWindow.resize(817, 648)
        self.centralwidget = QWidget(LogInWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formWidget = QWidget(self.centralwidget)
        self.formWidget.setObjectName(u"formWidget")
        self.formWidget.setGeometry(QRect(70, 50, 661, 341))
        self.gridLayout = QGridLayout(self.formWidget)
        self.gridLayout.setSpacing(9)
        self.gridLayout.setContentsMargins(16, 16, 16, 16)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(3)
        self.usernameLineEdit = QLineEdit(self.formWidget)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
        self.usernameLineEdit.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.gridLayout.addWidget(self.usernameLineEdit, 2, 1, 1, 1)

        self.passwordLineEdit = QLineEdit(self.formWidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setAutoFillBackground(False)
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.passwordLineEdit, 3, 1, 1, 1)

        self.passwordLabel = QLabel(self.formWidget)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.gridLayout.addWidget(self.passwordLabel, 3, 0, 1, 1)

        self.label = QLabel(self.formWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setPixmap(QPixmap(u"../../assets/logo.svg"))

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.usernameLabel = QLabel(self.formWidget)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.gridLayout.addWidget(self.usernameLabel, 2, 0, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.formWidget)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(7)
        self.commandLinkButton.setFont(font1)

        self.gridLayout.addWidget(self.commandLinkButton, 6, 1, 1, 1)

        self.radioButton = QRadioButton(self.formWidget)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout.addWidget(self.radioButton, 5, 0, 1, 1)

        self.pushButton = QPushButton(self.formWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 1)

        LogInWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(LogInWindow)
        self.statusbar.setObjectName(u"statusbar")
        LogInWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LogInWindow)

        QMetaObject.connectSlotsByName(LogInWindow)
    # setupUi

    def retranslateUi(self, LogInWindow):
        LogInWindow.setWindowTitle(QCoreApplication.translate("LogInWindow", u"MainWindow", None))
        self.usernameLineEdit.setPlaceholderText(QCoreApplication.translate("LogInWindow", u"Enter Your Username", None))
        self.passwordLineEdit.setText("")
        self.passwordLineEdit.setPlaceholderText(QCoreApplication.translate("LogInWindow", u"Enter Your Password", None))
        self.passwordLabel.setText(QCoreApplication.translate("LogInWindow", u"Password: ", None))
        self.label.setText("")
        self.usernameLabel.setText(QCoreApplication.translate("LogInWindow", u"Username: ", None))
        self.commandLinkButton.setText(QCoreApplication.translate("LogInWindow", u"New to CineDeck? Sign Up!", None))
        self.radioButton.setText(QCoreApplication.translate("LogInWindow", u"Remember Me?", None))
        self.pushButton.setText(QCoreApplication.translate("LogInWindow", u"Log In", None))
    # retranslateUi

