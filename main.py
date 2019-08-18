import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from MainWindow import Ui_MainWindow
from PyQt5.QtCore import QStringListModel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
import SignalToNoise
import cv2



class Camera(QtMultimedia.QCamera):
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
        return self.available_cam, i

    def getSupportedResolutions(self, cam):
        res_list = cam.supportedResolutions()
        for i in res_list:
            print(i)

    def getCameraCount(self, cam_dev):
        cam_id = 0


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    cam_index  = 0
    cam_count  = 0
    resolution = QtCore.QSize(0,0)
    dev_list = [] # Camera device list
    res_list = [] # Resolutions list
    cam_obj = Camera()
    dual_cam_flag = False


    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.slm = QStringListModel()

        cam_list, self.cam_count = self.cam_obj.getAvailableCameras()
        self.slm.setStringList(cam_list)
        self.listView_Devices.setModel(self.slm)
        self.label_device.setText("Devices("+str(self.cam_count)+")")

        # List the available Resulotions by the select camera
        self.listView_Devices.clicked.connect(self.clicked_device)

        # CheckBox stateChanged event
        self.checkBox_IsDualCam.stateChanged.connect(self.checkBox_DualCamChange)
        self.checkBox_CamFocus.stateChanged.connect(self.checkBox_CamFocusChange)

        # Open camera with the resolution selected
        # self.listWidget_resInfo.itemClicked.connect(self.setCameraResolution)
        self.listWidget_resInfo.itemClicked.connect(self.on_listWidget_resInfo_itemClicked)
        self.listWidget_resInfo.doubleClicked.connect(self.openCamera)

    def checkBox_DualCamChange(self):
        if self.checkBox_IsDualCam.checkState() == Qt.Checked:
            self.dual_cam_flag = True
            print("Is dual Camera? = ", self.dual_cam_flag)
        else:
            self.dual_cam_flag = False
            print("Is dual Camera? = ", self.dual_cam_flag)

    def checkBox_CamFocusChange(self):
        if self.checkBox_CamFocus.checkState() == Qt.Checked:
            pass
        else:
            pass



    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def clicked_device(self, index):
        self.cam_index = index.row()

        cam_selected = QtMultimedia.QCameraInfo.availableCameras()[index.row()]
        cam_obj = QtMultimedia.QCamera(cam_selected)
        cam_obj.load()
        print(cam_obj.status())
        if cam_obj.status() == 4:
            print("The camera is loaded and ready to be configured.")

        # Clear the items
        self.listWidget_resInfo.clear()

        # Add items to listview
        res= cam_obj.supportedViewfinderResolutions()
        for i in res:
            self.listWidget_resInfo.addItem(QListWidgetItem(str(i.width())+" * "+str(i.height())))

        self.label_Resolutions.setText("Resolutions("+str(self.listWidget_resInfo.count())+")")


    @QtCore.pyqtSlot(QtWidgets.QListWidgetItem)
    def on_listWidget_resInfo_itemClicked(self, item):
        # print(item.text())
        item_value = item.text()
        self.resolution.setWidth(int(item_value.split('*')[0]))
        self.resolution.setHeight(int(item_value.split('*')[1]))
        viewfinderSettings = QtMultimedia.QCameraViewfinderSettings()
        viewfinderSettings.setResolution(self.resolution)
        viewfinderSettings.setMaximumFrameRate(30.0);
        self.cam_obj.setViewfinderSettings(viewfinderSettings)
        print("resolution:", self.resolution.width(), self.resolution.height())


    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def openCamera(self, index):
        cap = cv2.VideoCapture(self.cam_index)

        for i in range(1,10,1):
            tmp, frame_base = cap.read()

        img_size  = frame_base.shape
        img_width = img_size[1]
        img_height= img_size[0]
        print(img_width, img_height)
        mid = int(img_width / 2)
        img_left = frame_base[0:img_height, 0:mid]
        cv2.namedWindow("Left_image",cv2.WINDOW_NORMAL)
        cv2.resizeWindow("left_image", mid, img_height)
        cv2.imshow("Left Eye", img_left)


        # while(cap.isOpened()):
        while(1):
            # ret, frame_test = cap.read()
            # psnr = SignalToNoise.compare_psnr(frame_base, frame_test)
            # # print(psnr)
            # if (ret) == True:
            #     # gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
            #     cv2.imshow('video', frame_test)
            # else:
            #     break

            if cv2.waitKey(1) & 0xFF == 27: #ESC
                cap.release()
                cv2.destroyAllWindows()
                break





if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_form = MainWindow()
    main_form.show()
    sys.exit(app.exec())

# if __name__=="__main__":
#     app = QtWidgets.QApplication(sys.argv)
#
#     c = QCamera()
#
#     print(c.availableDevices())
#     print(c.deviceDescription(c.availableDevices()[0]))
#     sys.exit(app.exec_())