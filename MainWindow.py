# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(697, 575)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_device = QtWidgets.QLabel(self.centralwidget)
        self.label_device.setGeometry(QtCore.QRect(70, 20, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_device.setFont(font)
        self.label_device.setObjectName("label_device")
        self.listView_resInfo = QtWidgets.QListView(self.centralwidget)
        self.listView_resInfo.setGeometry(QtCore.QRect(350, 60, 161, 461))
        self.listView_resInfo.setLineWidth(0)
        self.listView_resInfo.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView_resInfo.setObjectName("listView_resInfo")
        self.pushButton_refles = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_refles.setGeometry(QtCore.QRect(240, 260, 101, 61))
        self.pushButton_refles.setStyleSheet("border-image: url(:/LeftToRightImage/right_narrow.jpg);")
        self.pushButton_refles.setText("")
        self.pushButton_refles.setObjectName("pushButton_refles")
        self.listView_Devices = QtWidgets.QListView(self.centralwidget)
        self.listView_Devices.setGeometry(QtCore.QRect(10, 60, 221, 461))
        self.listView_Devices.setObjectName("listView_Devices")
        self.label_Resolutions = QtWidgets.QLabel(self.centralwidget)
        self.label_Resolutions.setGeometry(QtCore.QRect(370, 20, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Resolutions.setFont(font)
        self.label_Resolutions.setObjectName("label_Resolutions")
        self.checkBox_IsDualCam = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_IsDualCam.setGeometry(QtCore.QRect(550, 20, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(18)
        self.checkBox_IsDualCam.setFont(font)
        self.checkBox_IsDualCam.setObjectName("checkBox_IsDualCam")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 697, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_device.setText(_translate("MainWindow", "Devices"))
        self.label_Resolutions.setText(_translate("MainWindow", "Resolutions"))
        self.checkBox_IsDualCam.setText(_translate("MainWindow", "Dual Camera"))

import ImageSrc_rc
