# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
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
        self.label_device.setGeometry(QtCore.QRect(10, 20, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_device.setFont(font)
        self.label_device.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_device.setAlignment(QtCore.Qt.AlignCenter)
        self.label_device.setObjectName("label_device")
        self.listWidget_resInfo = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_resInfo.setGeometry(QtCore.QRect(350, 60, 141, 461))
        self.listWidget_resInfo.setLineWidth(0)
        self.listWidget_resInfo.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget_resInfo.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.listWidget_resInfo.setObjectName("listWidget_resInfo")
        self.pushButton_refles = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_refles.setGeometry(QtCore.QRect(240, 260, 101, 61))
        self.pushButton_refles.setStyleSheet("border-image: url(:/LeftToRightImage/right_narrow.jpg);")
        self.pushButton_refles.setText("")
        self.pushButton_refles.setObjectName("pushButton_refles")
        self.listView_Devices = QtWidgets.QListView(self.centralwidget)
        self.listView_Devices.setGeometry(QtCore.QRect(10, 60, 221, 461))
        self.listView_Devices.setObjectName("listView_Devices")
        self.label_Resolutions = QtWidgets.QLabel(self.centralwidget)
        self.label_Resolutions.setGeometry(QtCore.QRect(350, 20, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_Resolutions.setFont(font)
        self.label_Resolutions.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Resolutions.setObjectName("label_Resolutions")
        self.checkBox_IsDualCam = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_IsDualCam.setGeometry(QtCore.QRect(530, 60, 161, 31))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.checkBox_IsDualCam.setFont(font)
        self.checkBox_IsDualCam.setObjectName("checkBox_IsDualCam")
        self.checkBox_CamFocus = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_CamFocus.setGeometry(QtCore.QRect(530, 100, 161, 31))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_CamFocus.setFont(font)
        self.checkBox_CamFocus.setObjectName("checkBox_CamFocus")
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
        self.checkBox_CamFocus.setText(_translate("MainWindow", "Camera Focus"))
import ImageSrc_rc
