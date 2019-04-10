# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'father.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(482, 410)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 481, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(3, 41, 41, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(40, 40, 441, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(0, 70, 481, 291))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(50, 370, 75, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 370, 75, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 370, 75, 31))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.add)
        self.pushButton_2.clicked.connect(Dialog.delete)
        self.pushButton_3.clicked.connect(Dialog.import)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ff0000;\">常用地址收纳管理软件</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">搜索</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "添加"))
        self.pushButton_2.setText(_translate("Dialog", "删除"))
        self.pushButton_3.setText(_translate("Dialog", "导入"))

