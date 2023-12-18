# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstpage.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1439, 900)
        Form.setStyleSheet("QWidget#Form {\n"
"    border-radius: 24%;\n"
"}")
        self.toobar_label = QtWidgets.QLabel(Form)
        self.toobar_label.setGeometry(QtCore.QRect(0, 0, 80, 900))
        self.toobar_label.setStyleSheet("QLabel {\n"
"    background : #2e2e2e;\n"
"}\n"
"\n"
"")
        self.toobar_label.setText("")
        self.toobar_label.setObjectName("toobar_label")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(80, 0, 1360, 900))
        self.stackedWidget.setStyleSheet("QStackedWidget {\n"
"    border-top-right-radius: 24%;\n"
"}\n"
"\n"
"\n"
"QStackedWidget {\n"
"    border-bottom-right-radius: 24%;\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setStyleSheet("QWidget{\n"
"    background : #161616;\n"
"}")
        self.home_page.setObjectName("home_page")
        self.task_title_label = QtWidgets.QLabel(self.home_page)
        self.task_title_label.setGeometry(QtCore.QRect(37, 103, 61, 24))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.task_title_label.setFont(font)
        self.task_title_label.setStyleSheet("QLabel{\n"
"    color: #fff;\n"
"}")
        self.task_title_label.setObjectName("task_title_label")
        self.screen_widget = QtWidgets.QWidget(self.home_page)
        self.screen_widget.setGeometry(QtCore.QRect(15, 516, 252, 178))
        self.screen_widget.setStyleSheet("QWidget{\n"
"    border: 4px solid #ff9500;\n"
"    border-radius: 10px;\n"
"}")
        self.screen_widget.setObjectName("screen_widget")
        self.screen_label = QtWidgets.QLabel(self.screen_widget)
        self.screen_label.setGeometry(QtCore.QRect(0, 0, 252, 178))
        self.screen_label.setStyleSheet("")
        self.screen_label.setText("")
        self.screen_label.setScaledContents(True)
        self.screen_label.setObjectName("screen_label")
        self.footer_spline = QtWidgets.QLabel(self.home_page)
        self.footer_spline.setGeometry(QtCore.QRect(-3, 836, 282, 1))
        self.footer_spline.setStyleSheet("QLabel{\n"
"    background: #404040;\n"
"}")
        self.footer_spline.setText("")
        self.footer_spline.setObjectName("footer_spline")
        self.footer_text_label = QtWidgets.QLabel(self.home_page)
        self.footer_text_label.setGeometry(QtCore.QRect(41, 853, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.footer_text_label.setFont(font)
        self.footer_text_label.setStyleSheet("QLabel{\n"
"    color: #fff;\n"
"}")
        self.footer_text_label.setObjectName("footer_text_label")
        self.checkbox_widget_border = QtWidgets.QLabel(self.home_page)
        self.checkbox_widget_border.setGeometry(QtCore.QRect(-3, 450, 282, 2))
        self.checkbox_widget_border.setStyleSheet("QLabel{\n"
"    background: #fff;\n"
"}")
        self.checkbox_widget_border.setText("")
        self.checkbox_widget_border.setObjectName("checkbox_widget_border")
        self.combobox_label = QtWidgets.QLabel(self.home_page)
        self.combobox_label.setGeometry(QtCore.QRect(-3, 90, 282, 49))
        self.combobox_label.setStyleSheet("QLabel{\n"
"    border-top : 1px solid #404040;\n"
"    border-bottom : 1px solid #404040;\n"
"    background : #161616;\n"
"}\n"
"")
        self.combobox_label.setText("")
        self.combobox_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.combobox_label.setObjectName("combobox_label")
        self.assistant_title_label = QtWidgets.QLabel(self.home_page)
        self.assistant_title_label.setGeometry(QtCore.QRect(306, 50, 333, 21))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.assistant_title_label.setFont(font)
        self.assistant_title_label.setStyleSheet("QLabel{\n"
"    color: #fff;\n"
"}")
        self.assistant_title_label.setObjectName("assistant_title_label")
        self.assistant_spline = QtWidgets.QLabel(self.home_page)
        self.assistant_spline.setGeometry(QtCore.QRect(282, 90, 1078, 1))
        self.assistant_spline.setStyleSheet("QLabel{\n"
"    background: #404040;\n"
"}")
        self.assistant_spline.setText("")
        self.assistant_spline.setObjectName("assistant_spline")
        self.switch_checkbox = QtWidgets.QCheckBox(self.home_page)
        self.switch_checkbox.setGeometry(QtCore.QRect(242, 860, 40, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.switch_checkbox.setFont(font)
        self.switch_checkbox.setStyleSheet("/* Style for the QCheckBox */\n"
"QCheckBox::indicator {\n"
"    width : 40px;\n"
"    height : 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/assets/Switch1.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/assets/Switch 2.png);\n"
"    animation: toggleAnimation 0.5s ease-in-out;\n"
"}\n"
"\n"
"QCheckBox{\n"
"    color : #fff;\n"
"}\n"
"\n"
"/* Keyframe animation for the toggle effect */\n"
"@keyframes toggleAnimation {\n"
"    0% {\n"
"        transform: scale(1);\n"
"    }\n"
"    50% {\n"
"        transform: scale(1.2);\n"
"    }\n"
"    100% {\n"
"        transform: scale(1);\n"
"    }\n"
"}")
        self.switch_checkbox.setText("")
        self.switch_checkbox.setObjectName("switch_checkbox")
        self.message_widget = QtWidgets.QWidget(self.home_page)
        self.message_widget.setGeometry(QtCore.QRect(306, 741, 1030, 132))
        self.message_widget.setStyleSheet("QWidget{\n"
"    border: 1px solid #2e2e2e;\n"
"    border-radius: 24%;\n"
"}")
        self.message_widget.setObjectName("message_widget")
        self.messagebox_widget_spline = QtWidgets.QLabel(self.message_widget)
        self.messagebox_widget_spline.setGeometry(QtCore.QRect(0, 92, 1030, 1))
        self.messagebox_widget_spline.setStyleSheet("QLabel{\n"
"    background: #404040;\n"
"}")
        self.messagebox_widget_spline.setText("")
        self.messagebox_widget_spline.setObjectName("messagebox_widget_spline")
        self.pushButton = QtWidgets.QPushButton(self.message_widget)
        self.pushButton.setGeometry(QtCore.QRect(997, 102, 20, 20))
        self.pushButton.setStyleSheet("QPushButton {\n"
"        \n"
"    background-image: url(:/assets/Icon send.png);\n"
"        border : none;\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.message_content = QtWidgets.QTextEdit(self.message_widget)
        self.message_content.setGeometry(QtCore.QRect(16, 13, 998, 71))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        self.message_content.setFont(font)
        self.message_content.setStyleSheet("QTextEdit{\n"
"    color: #fff;\n"
"    border:none;\n"
"}")
        self.message_content.setObjectName("message_content")
        self.attachment_button = QtWidgets.QPushButton(self.message_widget)
        self.attachment_button.setGeometry(QtCore.QRect(20, 102, 20, 20))
        self.attachment_button.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-image: url(:/assets/Icon attachment.png);\n"
"}")
        self.attachment_button.setText("")
        self.attachment_button.setObjectName("attachment_button")
        self.attachment_button_2 = QtWidgets.QPushButton(self.message_widget)
        self.attachment_button_2.setGeometry(QtCore.QRect(940, 102, 20, 20))
        self.attachment_button_2.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-image: url(:/assets/Icon microphone.png);\n"
"}")
        self.attachment_button_2.setText("")
        self.attachment_button_2.setObjectName("attachment_button_2")
        self.header_label = QtWidgets.QLabel(self.home_page)
        self.header_label.setGeometry(QtCore.QRect(282, 0, 1078, 42))
        self.header_label.setStyleSheet("QLabel {\n"
"    background : #d68620;\n"
"}")
        self.header_label.setText("")
        self.header_label.setObjectName("header_label")
        self.head_titile = QtWidgets.QLabel(self.home_page)
        self.head_titile.setGeometry(QtCore.QRect(0, 0, 282, 41))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.head_titile.setFont(font)
        self.head_titile.setStyleSheet("QLabel {\n"
"    background : #d68620;\n"
"    color : #fff;\n"
"    border-right : 0.5px solid #808080;\n"
"}")
        self.head_titile.setText("")
        self.head_titile.setObjectName("head_titile")
        self.title_label = QtWidgets.QLabel(self.home_page)
        self.title_label.setGeometry(QtCore.QRect(24, 7, 234, 24))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("QLabel {\n"
"    color : #fff;\n"
"    background : none;\n"
"}")
        self.title_label.setObjectName("title_label")
        self.listWidget = QtWidgets.QListWidget(self.home_page)
        self.listWidget.setGeometry(QtCore.QRect(0, 139, 279, 311))
        self.listWidget.setStyleSheet("QListWidget {\n"
"    border: none;\n"
"}")
        self.listWidget.setObjectName("listWidget")
        self.expanded = QtWidgets.QCheckBox(self.home_page)
        self.expanded.setGeometry(QtCore.QRect(243, 107, 21, 17))
        self.expanded.setStyleSheet("/* Style for the QCheckBox */\n"
"QCheckBox::indicator {\n"
"    width : 20px;\n"
"    height : 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"   \n"
"    image: url(:/assets/Icon chevron down.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    \n"
"    image: url(:/assets/Icon chevron down - Copy.png);\n"
"}")
        self.expanded.setText("")
        self.expanded.setObjectName("expanded")
        self.chat_panel = QtWidgets.QWidget(self.home_page)
        self.chat_panel.setGeometry(QtCore.QRect(310, 100, 1021, 601))
        self.chat_panel.setStyleSheet("QWidget{\n"
"    border: 1px solid #2e2e2e;\n"
"    border-radius: 24%;\n"
"}")
        self.chat_panel.setObjectName("chat_panel")
        self.chat_list = QtWidgets.QListWidget(self.chat_panel)
        self.chat_list.setGeometry(QtCore.QRect(20, 10, 981, 581))
        self.chat_list.setStyleSheet("#chat_list{\n"
"    border:0px solid white;\n"
"}")
        self.chat_list.setObjectName("chat_list")
        self.combobox_label.raise_()
        self.task_title_label.raise_()
        self.screen_widget.raise_()
        self.footer_spline.raise_()
        self.footer_text_label.raise_()
        self.checkbox_widget_border.raise_()
        self.assistant_title_label.raise_()
        self.assistant_spline.raise_()
        self.switch_checkbox.raise_()
        self.message_widget.raise_()
        self.header_label.raise_()
        self.head_titile.raise_()
        self.title_label.raise_()
        self.listWidget.raise_()
        self.expanded.raise_()
        self.chat_panel.raise_()
        self.stackedWidget.addWidget(self.home_page)
        self.new_task_page = QtWidgets.QWidget()
        self.new_task_page.setStyleSheet("QWidget{\n"
"    background : #161616;\n"
"}")
        self.new_task_page.setObjectName("new_task_page")
        self.stackedWidget.addWidget(self.new_task_page)
        self.home_button = QtWidgets.QPushButton(Form)
        self.home_button.setGeometry(QtCore.QRect(30, 132, 20, 20))
        self.home_button.setStyleSheet("QPushButton {\n"
"        border : none;\n"
"background-image: url(:/assets/Icon home (1).png);\n"
"}\n"
"")
        self.home_button.setText("")
        self.home_button.setObjectName("home_button")
        self.message_button = QtWidgets.QPushButton(Form)
        self.message_button.setGeometry(QtCore.QRect(28, 179, 20, 20))
        self.message_button.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-image: url(:/assets/Icon message (2).png);\n"
"}")
        self.message_button.setText("")
        self.message_button.setObjectName("message_button")
        self.plus_new_task_button = QtWidgets.QPushButton(Form)
        self.plus_new_task_button.setGeometry(QtCore.QRect(30, 223, 20, 20))
        self.plus_new_task_button.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-image: url(:/assets/Icon plus task.png);\n"
"}")
        self.plus_new_task_button.setText("")
        self.plus_new_task_button.setObjectName("plus_new_task_button")
        self.info_button = QtWidgets.QPushButton(Form)
        self.info_button.setGeometry(QtCore.QRect(30, 848, 20, 20))
        self.info_button.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    background-image: url(:/assets/Icon info circle (1).png);\n"
"}")
        self.info_button.setText("")
        self.info_button.setObjectName("info_button")
        self.toolbar_splite_line = QtWidgets.QLabel(Form)
        self.toolbar_splite_line.setGeometry(QtCore.QRect(20, 826, 40, 2))
        self.toolbar_splite_line.setStyleSheet("QLabel{\n"
"    background: #404040;\n"
"}")
        self.toolbar_splite_line.setText("")
        self.toolbar_splite_line.setObjectName("toolbar_splite_line")

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.task_title_label.setText(_translate("Form", "TASKS"))
        self.footer_text_label.setText(_translate("Form", "Show AI Vision preview"))
        self.assistant_title_label.setText(_translate("Form", "OSVisualInstruct Assistant"))
        self.message_content.setPlaceholderText(_translate("Form", "Type your message here...."))
        self.title_label.setText(_translate("Form", "OSViusalInstruct"))
import resource_rc
