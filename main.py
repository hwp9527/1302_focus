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


class Camera(QtMultimedia.QCameraInfo):
    def __init__(self):
        super().__init__()

    def getAvailableCameras(self):
        available_cams = self.availableCameras()
        return available_cams

    def getSupportedResolutions(self, cam):
        res_list = cam.supportedResolutions()
        for i in res_list:
            print(i)

    def getCameraInfo(self, cam_dev):
        cam_id = 0


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    cam_index  = 0
    resolution = 0
    cam_info = Camera()
    cam_devs = cam_info.getAvailableCameras()

    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.slm = QStringListModel()
        self.cam_list = []

        # List the available camera devices
        for cam in self.cam_devs:
            self.cam_list.append(cam.description())
        print(self.cam_list)
        self.slm.setStringList(self.cam_list)
        self.listView_Devices.setModel(self.slm)

        # List the available Resulotions by the select camera
        self.listView_Devices.clicked.connect(self.clicked_device)

        # Open camera with the resolution selected
        self.listView_resInfo.doubleClicked.connect(self.clicked_resolution)

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def clicked_device(self, index):
        self.cam_index = index.row()
        res = []
        slm = QStringListModel()

        cam_selected = self.cam_devs[index.row()]
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
    def clicked_resolution(self, index):
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
