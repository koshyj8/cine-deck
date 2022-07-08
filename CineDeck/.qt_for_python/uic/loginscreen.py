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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(662, 358)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formWidget = QWidget(self.centralwidget)
        self.formWidget.setObjectName(u"formWidget")
        self.formWidget.setGeometry(QRect(240, 70, 292, 141))
        self.gridLayout = QGridLayout(self.formWidget)
        self.gridLayout.setSpacing(9)
        self.gridLayout.setContentsMargins(16, 16, 16, 16)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(3)
        self.usernameLabel = QLabel(self.formWidget)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.gridLayout.addWidget(self.usernameLabel, 0, 0, 1, 1)

        self.usernameLineEdit = QLineEdit(self.formWidget)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")

        self.gridLayout.addWidget(self.usernameLineEdit, 0, 1, 1, 1)

        self.passwordLabel = QLabel(self.formWidget)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.gridLayout.addWidget(self.passwordLabel, 1, 0, 1, 1)

        self.passwordLineEdit = QLineEdit(self.formWidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.passwordLineEdit, 1, 1, 1, 1)

        self.radioButton = QRadioButton(self.formWidget)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout.addWidget(self.radioButton, 2, 0, 1, 1)

        self.pushButton = QPushButton(self.formWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.formWidget)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(7)
        self.commandLinkButton.setFont(font)

        self.gridLayout.addWidget(self.commandLinkButton, 3, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(331, 30, 100, 45))
        font1 = QFont()
        font1.setPointSize(28)
        self.label.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 662, 22))
        self.menuLog_I = QMenu(self.menubar)
        self.menuLog_I.setObjectName(u"menuLog_I")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuLog_I.menuAction())
        self.menuLog_I.addSeparator()
        self.menuLog_I.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.usernameLabel.setText(QCoreApplication.translate("MainWindow", u"Username: ", None))
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"Password: ", None))
        self.passwordLineEdit.setText("")
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Remember Me?", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"New to CineDeck? Sign Up!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CineDeck", None))
        self.menuLog_I.setTitle(QCoreApplication.translate("MainWindow", u"Log In", None))
    # retranslateUi

