# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(933, 90)
        self.chat = QtWidgets.QFrame(Form)
        self.chat.setGeometry(QtCore.QRect(0, 0, 931, 91))
        self.chat.setStyleSheet("border:none;\n"
"color:white;\n"
"font-size:18px;")
        self.chat.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chat.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chat.setObjectName("chat")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.chat)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.avatar = QtWidgets.QLabel(self.chat)
        self.avatar.setMaximumSize(QtCore.QSize(70, 70))
        self.avatar.setAutoFillBackground(False)
        self.avatar.setStyleSheet("border:none;")
        self.avatar.setText("")
        self.avatar.setTextFormat(QtCore.Qt.PlainText)
        self.avatar.setPixmap(QtGui.QPixmap(":/assets/robot.png"))
        self.avatar.setScaledContents(True)
        self.avatar.setObjectName("avatar")
        self.horizontalLayout.addWidget(self.avatar)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.chat_user = QtWidgets.QLabel(self.chat)
        self.chat_user.setObjectName("chat_user")
        self.horizontalLayout_2.addWidget(self.chat_user)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.chat_time = QtWidgets.QLabel(self.chat)
        self.chat_time.setObjectName("chat_time")
        self.horizontalLayout_2.addWidget(self.chat_time)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.chat_content = QtWidgets.QLabel(self.chat)
        self.chat_content.setObjectName("chat_content")
        self.verticalLayout.addWidget(self.chat_content)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.avatar.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.chat_user.setText(_translate("Form", "Textasfasfasdfasfasdfasdfasfasdfasdfasdf"))
        self.chat_time.setText(_translate("Form", "TextLabel"))
        self.chat_content.setText(_translate("Form", "Text"))
import resource_rc
