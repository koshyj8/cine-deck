# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signupscreen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SignUpWindow(object):
    def setupUi(self, SignUpWindow):
        if not SignUpWindow.objectName():
            SignUpWindow.setObjectName(u"SignUpWindow")
        SignUpWindow.resize(523, 597)
        self.centralwidget = QWidget(SignUpWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 20, 464, 520))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.firstNameLabel = QLabel(self.formLayoutWidget)
        self.firstNameLabel.setObjectName(u"firstNameLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.firstNameLabel)

        self.firstNameLineEdit = QLineEdit(self.formLayoutWidget)
        self.firstNameLineEdit.setObjectName(u"firstNameLineEdit")
        self.firstNameLineEdit.setAutoFillBackground(False)
        self.firstNameLineEdit.setClearButtonEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.firstNameLineEdit)

        self.lastNameLabel = QLabel(self.formLayoutWidget)
        self.lastNameLabel.setObjectName(u"lastNameLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lastNameLabel)

        self.lastNameLineEdit = QLineEdit(self.formLayoutWidget)
        self.lastNameLineEdit.setObjectName(u"lastNameLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lastNameLineEdit)

        self.dateOfBirthLabel = QLabel(self.formLayoutWidget)
        self.dateOfBirthLabel.setObjectName(u"dateOfBirthLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.dateOfBirthLabel)

        self.usernameLabel = QLabel(self.formLayoutWidget)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.usernameLabel)

        self.usernameLineEdit = QLineEdit(self.formLayoutWidget)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.usernameLineEdit)

        self.passwordLabel = QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.passwordLabel)

        self.passwordLineEdit = QLineEdit(self.formLayoutWidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.passwordLineEdit)

        self.confirmPasswordLabel = QLabel(self.formLayoutWidget)
        self.confirmPasswordLabel.setObjectName(u"confirmPasswordLabel")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.confirmPasswordLabel)

        self.confirmPasswordLineEdit = QLineEdit(self.formLayoutWidget)
        self.confirmPasswordLineEdit.setObjectName(u"confirmPasswordLineEdit")
        self.confirmPasswordLineEdit.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.confirmPasswordLineEdit)

        self.pushButton = QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.pushButton)

        self.commandLinkButton = QCommandLinkButton(self.formLayoutWidget)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(7)
        self.commandLinkButton.setFont(font)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.commandLinkButton)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(28)
        self.label.setFont(font1)
        self.label.setPixmap(QPixmap(u"../../assets/logo.svg"))

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label)

        self.dateEdit = QDateEdit(self.formLayoutWidget)
        self.dateEdit.setObjectName(u"dateEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.dateEdit)

        SignUpWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SignUpWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 523, 22))
        self.menuSign_Up = QMenu(self.menubar)
        self.menuSign_Up.setObjectName(u"menuSign_Up")
        SignUpWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SignUpWindow)
        self.statusbar.setObjectName(u"statusbar")
        SignUpWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSign_Up.menuAction())

        self.retranslateUi(SignUpWindow)

        QMetaObject.connectSlotsByName(SignUpWindow)
    # setupUi

    def retranslateUi(self, SignUpWindow):
        SignUpWindow.setWindowTitle(QCoreApplication.translate("SignUpWindow", u"MainWindow", None))
        self.firstNameLabel.setText(QCoreApplication.translate("SignUpWindow", u"First Name: ", None))
#if QT_CONFIG(whatsthis)
        self.firstNameLineEdit.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.firstNameLineEdit.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.lastNameLabel.setText(QCoreApplication.translate("SignUpWindow", u"Last Name: ", None))
        self.dateOfBirthLabel.setText(QCoreApplication.translate("SignUpWindow", u"Date of Birth: ", None))
        self.usernameLabel.setText(QCoreApplication.translate("SignUpWindow", u"Username: ", None))
        self.passwordLabel.setText(QCoreApplication.translate("SignUpWindow", u"Password: ", None))
        self.passwordLineEdit.setText("")
        self.confirmPasswordLabel.setText(QCoreApplication.translate("SignUpWindow", u"Confirm Password: ", None))
        self.pushButton.setText(QCoreApplication.translate("SignUpWindow", u"Sign Up", None))
        self.commandLinkButton.setText(QCoreApplication.translate("SignUpWindow", u"Already have an account? Log In", None))
        self.label.setText("")
        self.menuSign_Up.setTitle(QCoreApplication.translate("SignUpWindow", u"Sign Up", None))
    # retranslateUi

