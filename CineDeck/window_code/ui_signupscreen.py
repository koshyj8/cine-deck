# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainscreenLnRtKu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
import os
import PyQt5
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import mysql.connector as mc
from qtwidgets import PasswordEdit


class Ui_SignUpWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
    def setupUi(self, SignUpWindow):
        if not SignUpWindow.objectName():
            SignUpWindow.setObjectName(u"SignUpWindow")
        SignUpWindow.showMaximized()
        self.centralwidget = QWidget(SignUpWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(130, 100, 635, 687))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.firstNameLabel = QLabel(self.formLayoutWidget)
        self.firstNameLabel.setObjectName(u"firstNameLabel")
        
        self.formLayout.setWidget(
            1, QFormLayout.LabelRole, self.firstNameLabel)

        self.firstNameLineEdit = QLineEdit(self.formLayoutWidget)
        self.firstNameLineEdit.setObjectName(u"firstNameLineEdit")
        self.firstNameLineEdit.setAutoFillBackground(False)
        self.firstNameLineEdit.setClearButtonEnabled(False)

        self.formLayout.setWidget(
            1, QFormLayout.FieldRole, self.firstNameLineEdit)

        self.lastNameLabel = QLabel(self.formLayoutWidget)
        self.lastNameLabel.setObjectName(u"lastNameLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lastNameLabel)

        self.lastNameLineEdit = QLineEdit(self.formLayoutWidget)
        self.lastNameLineEdit.setObjectName(u"lastNameLineEdit")

        self.formLayout.setWidget(
            2, QFormLayout.FieldRole, self.lastNameLineEdit)

        self.dateOfBirthLabel = QLabel(self.formLayoutWidget)
        self.dateOfBirthLabel.setObjectName(u"dateOfBirthLabel")

        self.formLayout.setWidget(
            3, QFormLayout.LabelRole, self.dateOfBirthLabel)
        font = QFont()
        self.dateEdit = QDateEdit(self.formLayoutWidget)
        self.dateEdit.isEnabled()
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(False)

        self.formLayout.setWidget(
            3, QFormLayout.FieldRole, self.dateEdit)

        self.usernameLabel = QLabel(self.formLayoutWidget)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.usernameLabel)

        self.usernameLineEdit = QLineEdit(self.formLayoutWidget)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")

        self.formLayout.setWidget(
            4, QFormLayout.FieldRole, self.usernameLineEdit)

        self.passwordLabel = QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.passwordLabel)

        self.passwordLineEdit = QLineEdit(self.formLayoutWidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(
            5, QFormLayout.FieldRole, self.passwordLineEdit)

        self.confirmPasswordLabel = QLabel(self.formLayoutWidget)
        self.confirmPasswordLabel.setObjectName(u"confirmPasswordLabel")

        self.formLayout.setWidget(
            6, QFormLayout.LabelRole, self.confirmPasswordLabel)

        self.confirmPasswordLineEdit = QLineEdit(self.formLayoutWidget)
        self.confirmPasswordLineEdit.setObjectName(u"confirmPasswordLineEdit")
        self.confirmPasswordLineEdit.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(
            6, QFormLayout.FieldRole, self.confirmPasswordLineEdit)

        self.commandLinkButton = QCommandLinkButton(self.formLayoutWidget)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(7)
        self.commandLinkButton.setFont(font)

        self.formLayout.setWidget(
            7, QFormLayout.FieldRole, self.commandLinkButton)

        self.pushButton = QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.pushButton)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(28)
        self.label.setFont(font1)
        self.label.setPixmap(QPixmap(r"CineDeck\assets\\logo.svg"))
        self.label.setGeometry(-30, -150, 600, 108)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label)
        SignUpWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(SignUpWindow)
        self.statusbar.setObjectName(u"statusbar")
        SignUpWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SignUpWindow)

        QMetaObject.connectSlotsByName(SignUpWindow)
    # setupUi
        self.pushButton.clicked.connect(self.createacc)
        self.commandLinkButton.clicked.connect(self.openloginwindow)
        
        self.firstNameLineEdit.setStyleSheet("background-color: #fff8e7; border-radius: 10px")
        self.lastNameLineEdit.setStyleSheet(
            "background-color: #fff8e7; border-radius: 10px")
        self.dateEdit.setStyleSheet(
            "alternate-background-color:  # fffff ; max-width: 720px; min-height: 100px")
        self.usernameLineEdit.setStyleSheet(
            "background-color: #fff8e7; border-radius: 10px")
        self.passwordLineEdit.setStyleSheet(
            "background-color: #fff8e7; border-radius: 10px")
        self.confirmPasswordLineEdit.setStyleSheet(
            "background-color: #fff8e7; border-radius: 10px")
        self.pushButton.setStyleSheet(
            "background-color: #fff8e7; border-style: inset; border-width: 2px; border-color: black")
    def createacc(self):
        first_name = self.firstNameLineEdit.text()
        last_name = self.lastNameLineEdit.text()
        if first_name and last_name and self.confirmPasswordLineEdit.text() and self.usernameLineEdit.text() is not None:
            
            if self.passwordLineEdit.text() == self.confirmPasswordLineEdit.text():
                password = self.confirmPasswordLineEdit.text()
                username = self.usernameLineEdit.text()
                dob = self.dateEdit.text()
                mydb = mc.connect(
                    host="localhost",
                    user="root",
                    password=os.getenv('mysqlpass'),
                    database="cinedeck")
                print('hi')
                mycursor = mydb.cursor()
                query = "SELECT username from user_info where username " \
                        "like '"+username+ "'"
                mycursor.execute(query)
                result = mycursor.fetchone()
                if result:
                    QtWidgets.QMessageBox.critical(
                        self, "Error", "Username already exists!")
                else:
                    insert = f'INSERT into user_info values("koshy", "john", "{username}", "{password}")'
                    mycursor.execute(insert)
                    QtWidgets.QMessageBox.information(
                        self, "Success ✅", "Successfully created CineDeck Account!")
            else:
                QtWidgets.QMessageBox.critical(self, "Error", "Passwords do not match!")
        else:
            QtWidgets.QMessageBox.critical(
                self, "Error", "Please Enter Details!")
        
    def openloginwindow(self):
        self.selfloginwindow.setupUi(self.selfloginwindow)
        
    def retranslateUi(self, SignUpWindow):
        SignUpWindow.setWindowTitle(QCoreApplication.translate(
            "SignUpWindow", u"CineDeck - Sign Up", None))
        self.firstNameLabel.setText(QCoreApplication.translate(
            "SignUpWindow", u"First Name: ", None))
#if QT_CONFIG(whatsthis)
        self.firstNameLineEdit.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.firstNameLineEdit.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.lastNameLabel.setText(QCoreApplication.translate(
            "SignUpWindow", u"Last Name: ", None))
        self.dateOfBirthLabel.setText(QCoreApplication.translate(
            "SignUpWindow", u"Date of Birth: ", None))
#if QT_CONFIG(whatsthis)
        self.dateEdit.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.dateEdit.setDisplayFormat(
            QCoreApplication.translate("SignUpWindow", u"d/M/yyyy", None))
        self.usernameLabel.setText(QCoreApplication.translate(
            "SignUpWindow", u"Username: ", None))
        self.passwordLabel.setText(QCoreApplication.translate(
            "SignUpWindow", u"Password: ", None))
        self.passwordLineEdit.setText("")
        self.confirmPasswordLabel.setText(QCoreApplication.translate(
            "SignUpWindow", u"Confirm Password: ", None))
        self.pushButton.setText(QCoreApplication.translate(
            "SignUpWindow", u"Sign Up", None))
        self.commandLinkButton.setText(QCoreApplication.translate(
            "SignUpWindow", u"Already have an account? Log In", None))
        self.label.setText("")
    # retranslateUi
