import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from MainWindow import Ui_MainWindow
from PyQt5.QtCore import QStringListModel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
import cv2


class Camera(QCamera):
    available_cam = []
    def __init__(self):
        super().__init__()

    def getAvailableCameras(self):
        # Return a string list
        i = 0
        available_dev = self.availableDevices()
        # print("len=", len(available_dev))
        while i < len(available_dev):
            self.available_cam.append(self.deviceDescription(self.availableDevices()[i]))
            i += 1
        return self.available_cam

    def getSupportedResolutions(self, cam):
        res_list = cam.supportedResolutions()
        for i in res_list:
            print(i)

    def getCameraInfo(self, cam_dev):
        cam_id = 0


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    cam_index  = 0
    resolution = 0
    cam_obj = Camera()

    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.slm = QStringListModel()

        self.slm.setStringList(self.cam_obj.getAvailableCameras())
        self.listView_Devices.setModel(self.slm)

        # List the available Resulotions by the select camera
        self.listView_Devices.clicked.connect(self.clicked_device)

        # Open camera with the resolution selected
        self.listView_resInfo.doubleClicked.connect(self.openCamera)

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def clicked_device(self, index):
        self.cam_index = index.row()
        res = []
        slm = QStringListModel()

        cam_selected = QtMultimedia.QCameraInfo.availableCameras()[index.row()]
        cam_obj = QCamera(cam_selected)
        cam_obj.load()
        print(cam_obj.status())
        if cam_obj.status() == 4:
            print("The camera is loaded and ready to be configured.")
        # img_capture = QCameraImageCapture(cam_obj)
        # resolutions = img_capture.supportedResolutions()
        resolutions = cam_obj.supportedViewfinderResolutions()
        print(resolutions)
        # print(len(resolutions[0]))
        for i in resolutions:
            print(i.width(), "*", i.height())
            res.append(str(i.width())+"*"+str(i.height()))
            slm.setStringList(res)
            self.listView_resInfo.setModel(slm)

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def openCamera(self, index):
        cap = cv2.VideoCapture(self.cam_index)

        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cv2.imshow('frame', gray)
            else:
                break

            if cv2.waitKey(1) & 0xFF == 27:
                cap.release()
                cv2.destroyAllWindows()
                break



if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_form = MainWindow()
    main_form.show()
    sys.exit(app.exec_())

# if __name__=="__main__":
#     app = QtWidgets.QApplication(sys.argv)
#
#     c = QCamera()
#
#     print(c.availableDevices())
#     print(c.deviceDescription(c.availableDevices()[0]))
#     sys.exit(app.exec_())