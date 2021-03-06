# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adduser.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import MainFrame
from DeviceinfoThread import DeviceInfoThread
from model.Device import DeviceInfo


class AddFriendDialog(object):

    Dialog = None
    main_window = None

    @staticmethod
    def init(main_window):
        AddFriendDialog.main_window = main_window
        AddFriendDialog.Dialog = QtWidgets.QDialog()
        AddFriendDialog.buttonBox = QtWidgets.QDialogButtonBox(AddFriendDialog.Dialog)
        AddFriendDialog.lineEdit = QtWidgets.QLineEdit(AddFriendDialog.Dialog)
        AddFriendDialog.label = QtWidgets.QLabel(AddFriendDialog.Dialog)
        AddFriendDialog.label_2 = QtWidgets.QLabel(AddFriendDialog.Dialog)
        AddFriendDialog.setupUi()

    @staticmethod
    def setupUi():
        AddFriendDialog.Dialog.setObjectName("Dialog")
        AddFriendDialog.Dialog.resize(321, 158)
        AddFriendDialog.buttonBox.setGeometry(QtCore.QRect(20, 110, 281, 32))
        AddFriendDialog.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        AddFriendDialog.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        AddFriendDialog.buttonBox.setObjectName("buttonBox")
        AddFriendDialog.lineEdit.setGeometry(QtCore.QRect(70, 70, 221, 21))
        AddFriendDialog.lineEdit.setText("")
        AddFriendDialog.lineEdit.setObjectName("lineEdit")
        AddFriendDialog.label.setGeometry(QtCore.QRect(20, 20, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        AddFriendDialog.label.setFont(font)
        AddFriendDialog.label.setTextFormat(QtCore.Qt.PlainText)
        AddFriendDialog.label.setAlignment(QtCore.Qt.AlignCenter)
        AddFriendDialog.label.setObjectName("label")
        AddFriendDialog.label_2.setGeometry(QtCore.QRect(30, 70, 60, 16))
        AddFriendDialog.label_2.setObjectName("label_2")

        AddFriendDialog.retranslateUi()
        AddFriendDialog.buttonBox.accepted.connect(AddFriendDialog.ok_btn_click)
        AddFriendDialog.buttonBox.rejected.connect(AddFriendDialog.cancel_btn_click)
        QtCore.QMetaObject.connectSlotsByName(AddFriendDialog.Dialog)

    @staticmethod
    def retranslateUi():
        _translate = QtCore.QCoreApplication.translate
        AddFriendDialog.Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        AddFriendDialog.label.setText(_translate("Dialog", "Add Friend"))
        AddFriendDialog.label_2.setText(_translate("Dialog", "I D"))



    @staticmethod
    def widget_show():
        AddFriendDialog.Dialog.show()

    @staticmethod
    def widget_hide():
        AddFriendDialog.Dialog.hide()

    @staticmethod
    def ok_btn_click():

        DeviceInfoThread.friend_device_info.append(DeviceInfo(AddFriendDialog.lineEdit.text(), AddFriendDialog.lineEdit.text()))

        AddFriendDialog.main_window.listwidget_item()
        AddFriendDialog.widget_hide()

    @staticmethod
    def cancel_btn_click():
        AddFriendDialog.widget_hide()
