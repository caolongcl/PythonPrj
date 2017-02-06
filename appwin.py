# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appwin.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os,json
import sendemail

class Ui_AppWin(object):
    def setupUi(self, AppWin):
        AppWin.setObjectName("AppWin")
        AppWin.resize(800, 268)
        AppWin.setMinimumSize(800, 228)
        AppWin.setMaximumSize(800, 228)
        self.centralwidget = QtWidgets.QWidget(AppWin)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 20, 751, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.layout_user = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.layout_user.setContentsMargins(0, 0, 0, 0)
        self.layout_user.setObjectName("layout_user")
        self.frame_user = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame_user.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_user.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_user.setObjectName("frame_user")
        self.label = QtWidgets.QLabel(self.frame_user)
        self.label.setGeometry(QtCore.QRect(20, 50, 31, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_user)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 31, 21))
        self.label_2.setObjectName("label_2")
        self.user_info_save = QtWidgets.QPushButton(self.frame_user)
        self.user_info_save.setGeometry(QtCore.QRect(460, 20, 75, 51))
        self.user_info_save.setObjectName("user_info_save")
        self.user_email = QtWidgets.QLineEdit(self.frame_user)
        self.user_email.setGeometry(QtCore.QRect(60, 50, 381, 20))
        self.user_email.setObjectName("user_email")
        self.user_password = QtWidgets.QLineEdit(self.frame_user)
        self.user_password.setGeometry(QtCore.QRect(60, 80, 381, 20))
        self.user_password.setObjectName("user_password")
        self.label_3 = QtWidgets.QLabel(self.frame_user)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 31, 21))
        self.label_3.setObjectName("label_3")
        self.email_list = QtWidgets.QLineEdit(self.frame_user)
        self.email_list.setGeometry(QtCore.QRect(60, 110, 381, 20))
        self.email_list.setObjectName("email_list")
        self.user_info_send = QtWidgets.QPushButton(self.frame_user)
        self.user_info_send.setGeometry(QtCore.QRect(460, 80, 75, 51))
        self.user_info_send.setObjectName("user_info_send")
        self.user_name = QtWidgets.QLineEdit(self.frame_user)
        self.user_name.setGeometry(QtCore.QRect(60, 20, 381, 20))
        self.user_name.setObjectName("user_name")
        self.label_4 = QtWidgets.QLabel(self.frame_user)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 31, 21))
        self.label_4.setObjectName("label_4")
        self.email_port = QtWidgets.QLabel(self.frame_user)
        self.email_port.setGeometry(QtCore.QRect(560, 80, 31, 21))
        self.email_port.setObjectName("email_port")
        self.email_server = QtWidgets.QLabel(self.frame_user)
        self.email_server.setGeometry(QtCore.QRect(560, 20, 61, 21))
        self.email_server.setObjectName("email_server")
        self.send_server = QtWidgets.QLineEdit(self.frame_user)
        self.send_server.setGeometry(QtCore.QRect(560, 40, 171, 20))
        self.send_server.setObjectName("send_server")
        self.send_port = QtWidgets.QLineEdit(self.frame_user)
        self.send_port.setGeometry(QtCore.QRect(560, 100, 171, 20))
        self.send_port.setObjectName("send_port")
        self.status = QtWidgets.QLabel(self.frame_user)
        self.status.setGeometry(QtCore.QRect(60, 160, 381, 16))
        self.status.setText("")
        self.status.setObjectName("status")
        self.layout_user.addWidget(self.frame_user, 0, 0, 1, 1)
        AppWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AppWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        AppWin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AppWin)
        self.statusbar.setObjectName("statusbar")
        AppWin.setStatusBar(self.statusbar)

        self.retranslateUi(AppWin)
        self.user_info_save.clicked.connect(self.saveInfo)
        self.user_info_send.clicked.connect(self.sendFile)
        QtCore.QMetaObject.connectSlotsByName(AppWin)

    def retranslateUi(self, AppWin):
        _translate = QtCore.QCoreApplication.translate
        AppWin.setWindowTitle(_translate("AppWin", "自动发送邮件工具"))
        self.label.setText(_translate("AppWin", "邮箱"))
        self.label_2.setText(_translate("AppWin", "密码"))
        self.user_info_save.setText(_translate("AppWin", "保存"))
        self.label_3.setText(_translate("AppWin", "文件"))
        self.user_info_send.setText(_translate("AppWin", "发送"))
        self.label_4.setText(_translate("AppWin", "姓名"))
        self.email_port.setText(_translate("AppWin", "端口"))
        self.email_server.setText(_translate("AppWin", "邮件服务器"))

    def saveInfo(self):
        self.status.setText('保存配置')
        self.updateConfigFile()

    def sendFile(self):
        self.status.setText('开始发送')
        # 准备发送者信息
        self.sendemailObj = sendemail.sendemail(self.config['username'],
                                      self.config['useremail'],
                                      self.config['userpassword'],
                                      self.config['emaillist'],
                                      self.config['sendserver'],
                                      self.config['sendport'])
        if self.sendemailObj:
            if self.sendemailObj.send():
                self.status.setText('发送成功')
            else:
                self.status.setText('发送失败')
        else:
            self.status.setText('发送失败')

    def initial(self):
        # 信息显示
        self.status.setText("文件一栏为"+"config\\file.xls" + ",且本程序所在目录下有config\\file.xls!")
        self.config = self.openConfigFile()
        self.user_name.setText(self.config['username'])
        self.user_email.setText(self.config['useremail'])
        self.user_password.setText(self.config['userpassword'])
        self.email_list.setText(self.config['emaillist'])
        self.send_server.setText(self.config['sendserver'])
        self.send_port.setText(str(self.config['sendport']))

    def isConfigFileExit(self, file):
        self.path = os.path.abspath('.') + "\\" + file
        return os.path.isfile(self.path)

    def openConfigFile(self, file='config\\config.json'):
        if self.isConfigFileExit(file):
            with open(file) as json_file:
                data = json.load(json_file)
                return data
        else:
            with open(file, 'w') as json_file:
                json_s = {
                    'username': 'xxx',
                    'useremail': 'xxxxxxx@qq.com',
                    'userpassword': '*******',
                    'emaillist': 'config\\file.xls',
                    'sendserver': 'smtp.qq.com',
                    'sendport': 587
                }
                encode_json = json.dumps(json_s)
                json_file.write(encode_json)
                return json_s

    def updateConfigFile(self, file='config\\config.json'):
        data = {}
        data['username'] = self.user_name.text()
        data['useremail'] = self.user_email.text()
        data['userpassword'] = self.user_password.text()
        data['emaillist'] = self.email_list.text()
        data['sendserver'] = self.send_server.text()
        data['sendport'] = int(self.send_port.text())
        self.config = data
        # print(data)
        with open(file, 'w') as json_file:
            return json_file.write(json.dumps(data))